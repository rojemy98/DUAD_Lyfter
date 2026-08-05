from repositories.products_repository import ProductsRepository
from repositories.invoices_repository import InvoicesRepository
from repositories.invoice_products_repository import InvoiceProductsRepository
from decimal import Decimal


class PurchaseService:

    def __init__(
        self,
        session,
        products_repo: ProductsRepository,
        invoices_repo: InvoicesRepository,
        invoice_products_repo: InvoiceProductsRepository
    ):

        self.session = session
        self.products_repo = products_repo
        self.invoices_repo = invoices_repo
        self.invoice_products_repo = invoice_products_repo


    def purchase(self, user_id: int, products: list):

        try:

            if not products:
                raise ValueError("Products list cannot be empty.")

            total = Decimal("0.00")
            invoice_details = []

            for item in products:

                product_id = item.get("product_id")
                quantity = item.get("quantity")

                if product_id is None or quantity is None:
                    raise ValueError(
                        "Each product must contain product_id and quantity."
                    )

                if quantity <= 0:
                    raise ValueError(
                        "Quantity must be greater than zero."
                    )

                product = self.products_repo.get_product_by_id(product_id)

                if product.quantity < quantity:
                    raise ValueError(
                        f"Not enough stock for product '{product.name}'."
                    )

                subtotal = product.price * quantity

                total += subtotal

                product.quantity -= quantity

                invoice_details.append(
                    {
                        "product": product,
                        "quantity": quantity,
                        "unit_price": product.price,
                        "subtotal": subtotal
                    }
                )

            invoice = self.invoices_repo.create_invoice(
                user_id=user_id,
                total=total
            )

            for item in invoice_details:

                self.invoice_products_repo.create_invoice_product(
                    invoice_id=invoice.id,
                    product_id=item["product"].id,
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                    subtotal=item["subtotal"]
                )

            self.session.commit()

            self.session.refresh(invoice)

            return invoice

        except Exception:

            self.session.rollback()

            raise