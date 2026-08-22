from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models.invoice import Invoice
from models.invoice_product import InvoiceProduct
from repositories.base_repository import BaseRepository


class InvoicesRepository(BaseRepository[Invoice]):

    def __init__(self, session: Session):
        super().__init__(session, Invoice)

    def get_by_number(
        self,
        invoice_number: str
    ) -> Invoice | None:

        statement = (
            select(self.model)
            .where(
                self.model.invoice_number == invoice_number
            )
            .options(
                selectinload(self.model.billing_address),
                selectinload(self.model.payment),
                selectinload(self.model.invoice_products)
                .selectinload(InvoiceProduct.product),
                selectinload(self.model.returns)
            )
        )

        return self.session.execute(
            statement
        ).scalar_one_or_none()

    def get_by_id_with_details(
        self,
        invoice_id: int
    ) -> Invoice | None:

        statement = (
            select(self.model)
            .where(
                self.model.id == invoice_id
            )
            .options(
                selectinload(self.model.billing_address),
                selectinload(self.model.payment),
                selectinload(self.model.invoice_products)
                .selectinload(InvoiceProduct.product),
                selectinload(self.model.returns)
            )
        )

        return self.session.execute(
            statement
        ).scalar_one_or_none()

    def get_by_user(
        self,
        user_id: int
    ) -> list[Invoice]:

        statement = (
            select(self.model)
            .where(
                self.model.user_id == user_id
            )
            .options(
                selectinload(self.model.billing_address),
                selectinload(self.model.payment),
                selectinload(self.model.invoice_products)
                .selectinload(InvoiceProduct.product)
            )
            .order_by(
                self.model.purchase_date.desc()
            )
        )

        return list(
            self.session.execute(
                statement
            ).scalars().all()
        )

    def get_by_number_and_user(
        self,
        invoice_number: str,
        user_id: int
    ) -> Invoice | None:

        statement = (
            select(self.model)
            .where(
                self.model.invoice_number == invoice_number,
                self.model.user_id == user_id
            )
            .options(
                selectinload(self.model.billing_address),
                selectinload(self.model.payment),
                selectinload(self.model.invoice_products)
                .selectinload(InvoiceProduct.product),
                selectinload(self.model.returns)
            )
        )

        return self.session.execute(
            statement
        ).scalar_one_or_none()