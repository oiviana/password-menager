from datetime import datetime
from pathlib import Path

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent 
    DB_DIR = BASE_DIR / 'db'

    def save(self):
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')

        if not table_path.exists():
            table_path.touch()


class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.created_at = datetime.now().isoformat()


p1 = Password(domain='111', password='2323')
p1.save()