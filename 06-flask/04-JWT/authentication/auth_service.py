import jwt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PRIVATE_KEY_PATH = BASE_DIR / "keys" / "private.pem"
PUBLIC_KEY_PATH = BASE_DIR / "keys" / "public.pem"

with open(PRIVATE_KEY_PATH, "r") as f:
    PRIVATE_KEY = f.read()

with open(PUBLIC_KEY_PATH, "r") as f:
    PUBLIC_KEY = f.read()

class JWT_Manager:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def encode(self, data):
        try:
            encoded = jwt.encode(data, PRIVATE_KEY, algorithm=self.algorithm)
            return encoded
        except:
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, PUBLIC_KEY, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None