from repositories.base_repository import BaseRepository
from database.models import InvoiceProduct


class InvoiceProductsRepository(BaseRepository):

    model = InvoiceProduct

    def create_invoice_product(
        self,
        invoice_id,
        product_id,
        quantity,
        unit_price,
        subtotal
    ):

        invoice_product = InvoiceProduct(
            invoice_id = invoice_id,
            product_id = product_id,
            quantity = quantity,
            unit_price = unit_price,
            subtotal = subtotal
        )

        self.session.add(invoice_product)

        return invoice_product