from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import session
from app.controller import get_user_details, create_user_data, get_all_users, update_user_data, delete_user, \
    delete_user_data
from app.schema import UserCreate, UserResponse
from typing import List

router = APIRouter(prefix= '/users', tags=['users'])

def get_db():
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()


@router.get('/', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db=db)

@router.get('/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_details(db, user_id)

@router.post('/', response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_data(db, user)

@router.put('/{user_id}')
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_data( user_id, db, user)

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_data( db, user_id)