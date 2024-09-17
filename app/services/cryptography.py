from os import getenv

from cryptography.fernet import Fernet


class EncryptionService:
    def __init__(self) -> None:

        self.encoded_key = getenv('ENCRYPTION_KEY').encode()
        self.encryption_key = self.encoded_key
        self.encryptor = Fernet(self.encryption_key)

    def encrypt_string(self, str_to_encrypt: str) -> str | None:
        """Receives a string, returns it encrypted if no error.
        Else return None.

        Args:
            str_to_encrypt (str): string to encrypt

        Returns:
            str | None: encrypted string or None
        """

        try:

            encoded_string = str_to_encrypt.encode()
            encrypted_string = self.encryptor.encrypt(encoded_string)
            
            return encrypted_string
        except Exception as e:
            return None
    
    def decrypt_string(self, str_to_decrypt: str) -> str | None:
        """Receives encrypted string, returns it decrypted if not error.
        Else return None.

        Args:
            str_to_decrypt (str): encrypted string to decrypt

        Returns:
            str | None: decrypted string or None
        """

        try:
            decrypted_string = self.encryptor.decrypt(str_to_decrypt)
            return decrypted_string.decode()

        except Exception as e:
            return None
