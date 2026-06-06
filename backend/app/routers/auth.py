from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import authenticate_admin, create_access_token
from app.database import get_db
from app.schemas import AdminLogin, Token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def admin_login(payload: AdminLogin, db: Session = Depends(get_db)):
    user = authenticate_admin(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    token = create_access_token(user.email)
    return {"access_token": token, "token_type": "bearer"}
