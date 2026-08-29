from sqlalchemy.orm import Session

from models import Return, ReturnProduct
from repositories import (
    ReturnsRepository,
    ReturnProductsRepository,
    InvoicesRepository
)


class ReturnService:

    def __init__(self, session: Session):
        self.session = session

        self.returns_repository = (
            ReturnsRepository(session)
        )

        self.return_products_repository = (
            ReturnProductsRepository(session)
        )

        self.invoices_repository = (
            InvoicesRepository(session)
        )

    def create_return(
        self,
        invoice_number: str,
        user_id: int,
        reason: str,
        products: list[dict]
    ) -> Return:

        invoice = (
            self.invoices_repository
            .get_by_invoice_number(
                invoice_number
            )
        )

        if invoice is None:
            raise LookupError(
                "Invoice not found."
            )

        if invoice.user_id != user_id:
            raise PermissionError(
                "You do not have access to this invoice."
            )

        if invoice.status not in {
            "PAID",
            "PARTIALLY_REFUNDED"
        }:
            raise ValueError(
                "This invoice cannot be returned."
            )

        if not reason or not reason.strip():
            raise ValueError(
                "Return reason is required."
            )

        if not products:
            raise ValueError(
                "At least one product is required."
            )

        validated_products = []

        for item in products:

            invoice_product_id = item.get(
                "invoice_product_id"
            )

            quantity = item.get(
                "quantity"
            )

            self._validate_quantity(quantity)

            invoice_product = next(
                (
                    product
                    for product
                    in invoice.invoice_products
                    if product.id
                    == invoice_product_id
                ),
                None
            )

            if invoice_product is None:
                raise ValueError(
                    f"Invoice product "
                    f"{invoice_product_id} "
                    f"does not belong to this invoice."
                )

            already_returned = (
                self.returns_repository
                .get_completed_quantity(
                    invoice_product.id
                )
            )

            available_quantity = (
                invoice_product.quantity
                - already_returned
            )

            if quantity > available_quantity:
                raise ValueError(
                    f"Cannot return {quantity} units "
                    f"of invoice product "
                    f"{invoice_product.id}. "
                    f"Only {available_quantity} "
                    f"can still be returned."
                )

            validated_products.append({
                "invoice_product": invoice_product,
                "quantity": quantity
            })

        try:
            return_request = Return(
                invoice_id=invoice.id,
                reason=reason.strip(),
                status="REQUESTED"
            )

            self.returns_repository.create(
                return_request
            )

            self.session.flush()

            for item in validated_products:

                return_product = ReturnProduct(
                    return_id=return_request.id,
                    invoice_product_id=(
                        item["invoice_product"].id
                    ),
                    quantity=item["quantity"]
                )

                self.return_products_repository.create(
                    return_product
                )

            self.session.commit()

            return (
                self.returns_repository
                .get_with_products(
                    return_request.id
                )
            )

        except Exception:
            self.session.rollback()
            raise

    def update_return_status(
        self,
        return_id: int,
        new_status: str
    ) -> Return:

        return_request = (
            self.returns_repository
            .get_with_products(return_id)
        )

        if return_request is None:
            raise LookupError(
                "Return request not found."
            )

        new_status = new_status.upper()

        allowed_transitions = {
            "REQUESTED": {
                "APPROVED",
                "REJECTED"
            },
            "APPROVED": {
                "COMPLETED"
            },
            "REJECTED": set(),
            "COMPLETED": set()
        }

        allowed_statuses = (
            allowed_transitions.get(
                return_request.status,
                set()
            )
        )

        if new_status not in allowed_statuses:
            raise ValueError(
                f"Cannot change return status "
                f"from {return_request.status} "
                f"to {new_status}."
            )

        try:

            if new_status == "COMPLETED":

                return_request.status = "COMPLETED"

                self.session.flush()

                self._complete_return(
                    return_request
                )

            else:
                return_request.status = new_status

            self.session.commit()

            return (
                self.returns_repository
                .get_with_products(return_id)
            )

        except Exception:
            self.session.rollback()
            raise

    def _calculate_invoice_status(
        self,
        invoice
    ) -> str:

        all_returned = True

        for invoice_product in (
            invoice.invoice_products
        ):

            returned_quantity = (
                self.returns_repository
                .get_completed_quantity(
                    invoice_product.id
                )
            )

            if (
                returned_quantity
                < invoice_product.quantity
            ):
                all_returned = False
                break

        if all_returned:
            return "REFUNDED"

        return "PARTIALLY_REFUNDED"
    
    @staticmethod
    def _validate_quantity(quantity: int) -> None:

        if (
            isinstance(quantity, bool)
            or not isinstance(quantity, int)
        ):
            raise ValueError(
                "Quantity must be an integer."
            )

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

    def _complete_return(
        self,
        return_request: Return
    ) -> None:

        invoice = (
            self.invoices_repository
            .get_by_id_with_details(
                return_request.invoice_id
            )
        )

        if invoice is None:
            raise LookupError(
                "Invoice not found."
            )

        for return_product in return_request.return_products:

            invoice_product = (
                return_product.invoice_product
            )

            if invoice_product is None:
                raise LookupError(
                    "Invoice product not found."
                )

            completed_quantity = (
                self.returns_repository
                .get_completed_quantity(
                    invoice_product.id
                )
            )

            previously_returned = (
                completed_quantity
                - return_product.quantity
            )

            remaining = (
                invoice_product.quantity
                - previously_returned
            )

            if return_product.quantity > remaining:
                raise ValueError(
                    f"Cannot complete return for "
                    f"invoice product {invoice_product.id}. "
                    f"Only {remaining} units remain returnable."
                )

            product = invoice_product.product

            if product is None:
                raise LookupError(
                    "Product not found."
                )

            product.stock += return_product.quantity

        self.session.flush()

        invoice.status = (
            self._calculate_invoice_status(invoice)
        )