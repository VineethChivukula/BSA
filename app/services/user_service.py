from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def register(data):
        UserRepository.add_user(data)
