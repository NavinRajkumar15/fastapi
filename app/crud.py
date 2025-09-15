from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserResponse
from fastapi import HTTPException

def get_all_users_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db:Session, user:UserCreate ) -> User:
    user = User(name = user.name, email = user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> UserResponse | None:
    user_data = db.query(User).filter(User.id == user_id).first()

    return user_data

def update_user(db:Session, user_id: int, user: UserCreate) -> UserResponse:
    data = db.query(User).filter(User.id == user_id).first()

    if not data:
        raise HTTPException(status_code=404, detail="User not found")

    data.name = user.name
    data.email = user.email

    db.commit()
    db.refresh(data)
    return data


def delete_user(db:Session, user_id: int):
    data = db.query(User).filter(User.id == user_id).first()

    if not data:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(data)
    db.commit()

    return None