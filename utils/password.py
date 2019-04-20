import base64
import bcrypt
import hashlib

class PasswordHandler:

    @staticmethod
    def pw_hash(password_string):
        bytes_password = password_string.encode()
        hashed_password = bcrypt.hashpw(
            base64.b64encode(hashlib.sha256(bytes_password).digest()),
            bcrypt.gensalt()
        )

        return hashed_password

    @staticmethod
    def pw_check(password_string, password_hash):
        return bcrypt.checkpw(password_string, password_hash)
