import string, secrets

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase

    @classmethod
    def _get_random_string(cls):
        string = ''
        for i in range(25):
           string += secrets.choice(cls.RANDOM_STRING_CHARS)
           print(string)
           
        return string


FernetHasher._get_random_string()