from sqlalchemy import select
from sqlalchemy.orm import Session

from models.billing_address import BillingAddress
from repositories.base_repository import BaseRepository


class BillingAddressesRepository(BaseRepository[BillingAddress]):

    def __init__(self, session: Session):
        super().__init__(session, BillingAddress)

    def get_by_user(
        self,
        user_id: int
    ) -> list[BillingAddress]:

        statement = select(self.model).where(
            self.model.user_id == user_id
        )

        return list(
            self.session.execute(
                statement
            ).scalars().all()
        )

    def get_by_id_and_user(
        self,
        address_id: int,
        user_id: int
    ) -> BillingAddress | None:

        statement = select(self.model).where(
            self.model.id == address_id,
            self.model.user_id == user_id
        )

        return self.session.execute(
            statement
        ).scalar_one_or_none()