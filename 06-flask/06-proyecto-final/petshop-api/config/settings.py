from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

KEYS_DIR = BASE_DIR / "keys"

PRIVATE_KEY_PATH = KEYS_DIR / "private.pem"
PUBLIC_KEY_PATH = KEYS_DIR / "public.pem"

JWT_ALGORITHM = "RS256"
JWT_ACCESS_TOKEN_EXPIRES = 900


def _load_key(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"JWT key not found: {path}"
        )

    return path.read_text(encoding="utf-8")


def load_private_key() -> str:
    return _load_key(PRIVATE_KEY_PATH)


def load_public_key() -> str:
    return _load_key(PUBLIC_KEY_PATH)