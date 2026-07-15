from database import DatabaseConnection
from models import Base

db = DatabaseConnection(
    user="postgres",
    password="Nyjah2022_",
    host="localhost",
    database="postgres",
    port=5432
)

engine = db.create_engine()

Base.metadata.create_all(engine)

print("Tables created successfully.")