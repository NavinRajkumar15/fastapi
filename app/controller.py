from app.crud import create_user, get_user, get_all_users_data, update_user, delete_user
from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserResponse
from typing import List

def get_all_users(db: Session) -> List[User]:
    return get_all_users_data(db)

def get_user_details(db: Session, user_id: int):
    return get_user(db, user_id=user_id)

def create_user_data(db: Session, user: UserCreate) -> UserResponse:
    user_data =  create_user(db, user)
    return UserResponse(name=user_data.name, id= user_data.id, email=user_data.email)

def update_user_data(user_id: int, db: Session, user: UserCreate):
    user_data = update_user(db, user_id, user)
    return UserResponse(name=user_data.name, id= user_data.id, email=user_data.email)

def delete_user_data(db: Session, user_id: int):
    return delete_user(db, user_id=user_id)