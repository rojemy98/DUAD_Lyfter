from sqlalchemy import select
from sqlalchemy.orm import selectinload
from repositories.base_repository import BaseRepository
from database.models import Invoice, InvoiceProduct


class InvoicesRepository(BaseRepository):

    model = Invoice

    def create_invoice(self, user_id: int, total):

        invoice = Invoice(
            user_id=user_id,
            total=total
        )

        self.session.add(invoice)

        self.session.flush()

        return invoice

    def get_invoices_by_user(self, user_id: int):

        statement = (
            select(Invoice)
            .options(
                selectinload(Invoice.products)
                .selectinload(InvoiceProduct.product)
            )
            .where(Invoice.user_id == user_id)
            .order_by(Invoice.purchase_date.desc())
        )

        return self.session.scalars(statement).all()

def get_all_invoices(self):

    statement = (
        select(Invoice)
        .options(
            selectinload(Invoice.products)
            .selectinload(InvoiceProduct.product)
        )
        .order_by(Invoice.id)
    )

    return self.session.scalars(statement).all()