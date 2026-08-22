from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models.return_model import Return
from models.return_product import ReturnProduct
from repositories.base_repository import BaseRepository


class ReturnsRepository(BaseRepository[Return]):

    def __init__(self, session: Session):
        super().__init__(session, Return)

    def get_by_invoice_id(
        self,
        invoice_id: int
    ) -> list[Return]:

        statement = (
            select(self.model)
            .where(
                self.model.invoice_id == invoice_id
            )
            .options(
                selectinload(self.model.return_products)
                .selectinload(ReturnProduct.invoice_product)
            )
            .order_by(
                self.model.created_at.desc()
            )
        )

        return list(
            self.session.execute(
                statement
            ).scalars().all()
        )

    def get_by_id_with_products(
        self,
        return_id: int
    ) -> Return | None:

        statement = (
            select(self.model)
            .where(
                self.model.id == return_id
            )
            .options(
                selectinload(self.model.return_products)
                .selectinload(ReturnProduct.invoice_product)
            )
        )

        return self.session.execute(
            statement
        ).scalar_one_or_none()

    def add_return_product(
        self,
        return_product: ReturnProduct
    ) -> ReturnProduct:

        self.session.add(return_product)
        self.session.flush()

        return return_product