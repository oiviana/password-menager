import string, secrets
import hashlib
import base64

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase

    @classmethod
    def _get_random_string(cls):
        string = ''
        for i in range(25):
           string += secrets.choice(cls.RANDOM_STRING_CHARS)

        return string
    
    @classmethod
    def create_key(cls):
        keyValue = cls._get_random_string()
        hasher = hashlib.sha256(keyValue.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        print(key)

FernetHasher.create_key()

# 00:39:13