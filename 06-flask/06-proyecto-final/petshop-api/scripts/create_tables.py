from database.db_manager import DatabaseManager
from models import (
    User,
    LoginHistory,
    Product,
    Cart,
    CartProduct,
    BillingAddress,
    Invoice,
    InvoiceProduct,
    Payment,
    Return,
    ReturnProduct,
)


DATABASE_URL = (
    "postgresql+psycopg://postgres:[password]@localhost:5432/postgres"
)


db_manager = DatabaseManager(DATABASE_URL)

db_manager.create_tables()

print("Database schema and tables created successfully.")

db_manager.close()