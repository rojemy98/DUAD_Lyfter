from sqlalchemy.orm import Session

from models import ReturnProduct
from repositories.base_repository import BaseRepository


class ReturnProductsRepository(
    BaseRepository[ReturnProduct]
):

    def __init__(self, session: Session):
        super().__init__(
            session,
            ReturnProduct
        )