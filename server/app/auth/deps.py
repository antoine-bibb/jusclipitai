from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.models import User

bearer = HTTPBearer()


def get_current_user(
    cred: HTTPAuthorizationCredentials = Depends(bearer), db: Session = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(cred.credentials, settings.secret_key, algorithms=['HS256'])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail='Invalid token') from exc

    user = db.query(User).filter(User.id == int(payload['sub'])).first()
    if not user:
        raise HTTPException(status_code=401, detail='User not found')
    return user
