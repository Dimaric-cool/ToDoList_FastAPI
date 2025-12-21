from sqlalchemy.orm import Session
from typing import Optional
from app.models.db.user import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create(self, email: str, hashed_password: str) -> UserModel:
        user_model = UserModel(email=email, hashed_password=hashed_password)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model