from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.security import create_token, hash_password, verify_password
from app.core.config import settings
from app.db.session import get_db
from app.models.models import PlanTier, Subscription, User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/register', response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail='Email already exists')
    user = User(email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    db.flush()
    db.add(Subscription(user_id=user.id, tier=PlanTier.FREE))
    db.commit()
    return _tokens(user.id)


@router.post('/login', response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    return _tokens(user.id)


def _tokens(user_id: int) -> TokenResponse:
    access = create_token(str(user_id), timedelta(minutes=settings.access_token_expire_minutes))
    refresh = create_token(str(user_id), timedelta(days=settings.refresh_token_expire_days))
    return TokenResponse(access_token=access, refresh_token=refresh)
