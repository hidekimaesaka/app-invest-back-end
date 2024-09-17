from app.repository.user import UserRepository

from app.services.cryptography import EncryptionService

class UserService:

    def __init__(self) -> None:
        self.user_repo = UserRepository()
        self.encryption_svc = EncryptionService()

    def validate_user_credentials(self, username: str, password: str) -> bool:
        """Validates if user login is correct.

        Args:
            username (str): username sent by user
            password (str): password sent by user

        Returns:
            bool: true if authenticated, false if not
        """

        try:
            user = self.user_repo.get_user_by_username(username)
            decrypted_password = self.encryption_svc.decrypt_string(user.password)

            credentials_is_correct = password == decrypted_password

            return credentials_is_correct

        except Exception as e:
            return False
