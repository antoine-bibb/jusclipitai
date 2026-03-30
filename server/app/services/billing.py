from fastapi import HTTPException
import stripe

from app.core.config import settings
from app.models.models import PlanTier, Subscription

stripe.api_key = settings.stripe_secret_key

PRICE_MAP = {
    PlanTier.PRO: settings.stripe_price_pro,
    PlanTier.BUSINESS: settings.stripe_price_business,
}


def create_checkout_session(subscription: Subscription, tier: PlanTier, user_id: int) -> str:
    price_id = PRICE_MAP.get(tier)
    if not price_id:
        raise HTTPException(status_code=400, detail='Unsupported tier')

    session = stripe.checkout.Session.create(
        mode='subscription',
        line_items=[{'price': price_id, 'quantity': 1}],
        success_url=f"{settings.frontend_url}/billing?status=success",
        cancel_url=f"{settings.frontend_url}/pricing?status=cancel",
        client_reference_id=str(user_id),
        customer=subscription.stripe_customer_id or None,
    )
    return session.url
