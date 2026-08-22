from datetime import datetime, UTC
from decimal import Decimal

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Numeric,
    String
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, SCHEMA_NAME


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(f"{SCHEMA_NAME}.users.id"),
        nullable=False
    )

    invoice_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    billing_address_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(f"{SCHEMA_NAME}.billing_addresses.id"),
        nullable=False
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="PAID"
    )

    purchase_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    __table_args__ = (
        CheckConstraint(
            "total >= 0",
            name="check_invoice_total"
        ),
        CheckConstraint(
            "status IN "
            "('PAID', 'CANCELLED', 'REFUNDED', 'PARTIALLY_REFUNDED')",
            name="check_invoice_status"
        ),
    )

    user = relationship(
        "User",
        back_populates="invoices"
    )

    billing_address = relationship(
        "BillingAddress",
        back_populates="invoices"
    )

    invoice_products = relationship(
        "InvoiceProduct",
        back_populates="invoice"
    )

    payment = relationship(
        "Payment",
        back_populates="invoice",
        uselist=False
    )

    returns = relationship(
        "Return",
        back_populates="invoice"
    )