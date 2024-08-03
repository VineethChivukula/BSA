from app.repositories.user_repository import UserRepository


class UserService:
    """
    Registers a user.

    Args:
        data (dict): A dictionary containing user data.

    Returns:
        None

    Raises:
        None
    """
    @staticmethod
    def register(data):
        UserRepository.add_user(data)
