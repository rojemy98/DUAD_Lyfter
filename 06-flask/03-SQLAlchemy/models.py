from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from typing import Optional


class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(String(120), unique=True)

    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    cars: Mapped[list["Car"]] = relationship(
        back_populates="user"
    )

class Address(Base):

    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)

    street: Mapped[str] = mapped_column(String(200))

    city: Mapped[str] = mapped_column(String(100))

    country: Mapped[str] = mapped_column(String(100))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id",ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship(
        back_populates="addresses"
    )

class Car(Base):

    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)

    brand: Mapped[str] = mapped_column(String(100))

    model: Mapped[str] = mapped_column(String(100))

    year: Mapped[int] = mapped_column()

    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    user: Mapped[Optional["User"]] = relationship(
        back_populates="cars"
    )