from app.models.user import User
from app.utils.db import db

class UserRepository:
    @staticmethod
    def add_user(data):
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_user_by_credentials(data):
        user = User.query.filter_by(email=data['email'], password=data['password']).first()
        return user
