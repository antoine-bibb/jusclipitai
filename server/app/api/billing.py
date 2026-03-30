from datetime import datetime

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session
import stripe

from app.auth.deps import get_current_user
from app.core.config import settings
from app.db.session import get_db
from app.models.models import PlanTier, Subscription, User
from app.services.billing import create_checkout_session

router = APIRouter(prefix='/billing', tags=['billing'])


@router.get('/status')
def billing_status(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Subscription).filter(Subscription.user_id == current_user.id).first()


@router.post('/checkout/{tier}')
def start_checkout(tier: PlanTier, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    sub = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    assert sub is not None
    return {'checkout_url': create_checkout_session(sub, tier, current_user.id)}


@router.post('/webhook')
async def stripe_webhook(
    request: Request,
    stripe_signature: str = Header(default=''),
    db: Session = Depends(get_db),
):
    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(payload=payload, sig_header=stripe_signature, secret=settings.stripe_webhook_secret)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail='Invalid webhook') from exc

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        user_id = int(session['client_reference_id'])
        sub = db.query(Subscription).filter(Subscription.user_id == user_id).first()
        if sub:
            sub.status = 'active'
            sub.stripe_customer_id = session.get('customer')
            sub.stripe_subscription_id = session.get('subscription')
            db.commit()
    if event['type'] == 'customer.subscription.updated':
        obj = event['data']['object']
        sub = db.query(Subscription).filter(Subscription.stripe_subscription_id == obj['id']).first()
        if sub:
            sub.status = obj.get('status', 'active')
            sub.current_period_start = datetime.fromtimestamp(obj.get('current_period_start'))
            sub.current_period_end = datetime.fromtimestamp(obj.get('current_period_end'))
            db.commit()

    return {'received': True}
