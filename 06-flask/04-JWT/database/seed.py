from datetime import UTC, datetime, timedelta
from decimal import Decimal
import random

from faker import Faker
from sqlalchemy.orm import Session

from database import DatabaseConnection
from models import (
    Base,
    User,
    Product,
    Invoice,
    InvoiceProduct,
    UserRole,
    InvoiceStatus,
)

db = DatabaseConnection(
    user="postgres",
    password="Nyjah2022_",
    host="localhost",
    database="postgres",
    port=5432
)

engine = db.create_engine()

fake = Faker()


def random_date(days_back: int = 365):
    return datetime.now(UTC) - timedelta(days=random.randint(0, days_back))


def seed():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        users = []

        # -----------------------------
        # USERS
        # -----------------------------
        admin = User(
            name="Admin",
            last_name="System",
            email="admin@test.com",
            password=fake.password(length=15),
            role=UserRole.ADMIN,
            registration_date=random_date(),
        )

        session.add(admin)
        users.append(admin)

        for i in range(49):

            user = User(
                name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                password=fake.password(length=16),
                role=UserRole.USER,
                registration_date=random_date(),
            )

            users.append(user)

        session.add_all(users)
        session.commit()

        # -----------------------------
        # PRODUCTS
        # -----------------------------

        fruits = [
            "Apple", "Banana", "Orange", "Pineapple", "Watermelon",
            "Strawberry", "Grape", "Pear", "Kiwi", "Peach",
            "Mango", "Papaya", "Cherry", "Blueberry", "Lemon",
            "Lime", "Coconut", "Plum", "Melon", "Guava",
            "Dragon Fruit", "Avocado", "Blackberry", "Raspberry",
            "Passion Fruit", "Fig", "Pomegranate", "Apricot",
            "Mandarin", "Tangerine", "Cranberry", "Lychee",
            "Jackfruit", "Starfruit", "Durian", "Persimmon",
            "Mulberry", "Gooseberry", "Date", "Olive",
            "Cantaloupe", "Nectarine", "Currant", "Quince",
            "Soursop", "Longan", "Sapodilla", "Tamarind",
            "Ugli Fruit", "Clementine"
        ]

        products = []

        for fruit in fruits:

            product = Product(
                name=fruit,
                price=Decimal(random.randint(100, 5000)),
                quantity=random.randint(20, 200),
                entry_date=random_date().date(),
            )

            products.append(product)

        session.add_all(products)
        session.commit()

        # -----------------------------
        # INVOICES
        # -----------------------------

        invoices = []

        for _ in range(30):

            invoice = Invoice(
                user=random.choice(users),
                purchase_date=random_date(120),
                total=Decimal("0.00"),
                status=InvoiceStatus.COMPLETED,
            )

            session.add(invoice)
            invoices.append(invoice)

        session.commit()

        # -----------------------------
        # INVOICE PRODUCTS
        # -----------------------------

        for invoice in invoices:

            selected_products = random.sample(
                products,
                random.randint(1, 5)
            )

            total = Decimal("0.00")

            for product in selected_products:

                quantity = random.randint(1, 5)

                if product.quantity < quantity:
                    continue

                subtotal = product.price * quantity

                detail = InvoiceProduct(
                    invoice=invoice,
                    product=product,
                    quantity=quantity,
                    unit_price=product.price,
                    subtotal=subtotal,
                )

                product.quantity -= quantity

                total += subtotal

                session.add(detail)

            invoice.total = total

        session.commit()

    print("Seed completed successfully!")


if __name__ == "__main__":
    seed()