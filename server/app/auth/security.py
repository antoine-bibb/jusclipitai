from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(sub: str, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)
    payload = {'sub': sub, 'iat': int(now.timestamp()), 'exp': int((now + expires_delta).timestamp())}
    return jwt.encode(payload, settings.secret_key, algorithm='HS256')
