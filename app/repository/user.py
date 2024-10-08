from sqlalchemy import select

from app.db import session

from app.services.cryptography import EncryptionService

from app.models.user import User


class UserRepository:

    def __init__(self) -> None:
        self.session = session

        self.encryption_svc = EncryptionService()

    def add_user(self, user_obj: dict) -> bool:
        """Receives a user dict object, and tries to register it on database.
        Args:
            user_obj (dict): object data that comes from creation request

        Returns:
            bool: true if created, false if not
        """

        new_user = User()
        new_user.name = user_obj['name']
        new_user.email = user_obj['email']
        new_user.username = user_obj['username']

        user_exists = self.__user_exists(new_user)

        if user_exists:
            return False
        
        # encrypt user's password
        encrypted_user_password = self.encryption_svc.encrypt_string(user_obj['password'])
        new_user.password = encrypted_user_password

        self.session.add(new_user)
        self.session.commit()

        return True


    def update_user(self, user_obj: dict) -> bool:
        """tries to update a user by given user_obj
        returns true if updated, false if not.

        Args:
            user_obj (dict): user object from the request

        Returns:
            bool: true if updated, false if not
        """

        username = user_obj['username']

        user_to_update = self.get_user_by_username(username)

        if not user_to_update:
            return False
        
        user_to_update.email = user_obj['email']
        user_to_update.name = user_obj['name']

        self.session.merge(user_to_update)
        self.session.commit()
        return True
    
    def delete_user(self, username: str) -> bool:
        """deletes a user by username

        Args:
            username (str): username string from request obj

        Returns:
            bool: true if deleted, false if not
        """
        
        user = self.get_user_by_username(username)
        if not user:
            return False

        self.session.delete(user)
        self.session.commit()
        return True
    
    def get_user_by_username(self, username: str) -> User | None:
        """searchs for a user on database by given username

        Args:
            username (str): username of a user

        Returns:
            User | None: user object, or None if error occurs
        """

        try:
            query = select(User).where(User.username == username)
            user = self.session.scalar(query)
            return user
        except Exception as e:
            return None
    
    def get_user_by_email(self, email: str) -> User | None:
        """searchs for a user on database by given email

        Args:
            email (str): email of a user

        Returns:
            User | None: user object, or None if error occurs
        """

        try:
            query = select(User).where(User.email == email)
            user = self.session.scalar(query)
            return user
        except Exception as e:
            return None

    def __user_exists(self, user: User) -> bool:
        """Receives an user object, and returns true if it exists, false
        if not.

        Args:
            user (User): User object

        Returns:
            bool: True if exists, false if not.
        """

        try:
            username = user.username
            email = user.email
            found_by_username = self.get_user_by_username(username)
            found_by_email = self.get_user_by_email(email)
            if found_by_username or found_by_email:
                return True

        except Exception as e:
            raise Exception

        return False
