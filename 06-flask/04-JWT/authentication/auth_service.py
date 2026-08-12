from datetime import datetime, timedelta, UTC
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

    def encode(self, data, expires_in: timedelta):

        payload = data.copy()

        payload["iat"] = datetime.now(UTC)
        payload["exp"] = datetime.now(UTC) + expires_in

        return jwt.encode(
            payload,
            PRIVATE_KEY,
            algorithm=self.algorithm
        )

    def decode(self, token):

        return jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=[self.algorithm]
        )