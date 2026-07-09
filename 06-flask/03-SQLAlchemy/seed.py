from faker import Faker
from sqlalchemy.orm import Session
from database import Database
from models import Base
from models import User
from models import Address
from models import Car

import random

fake = Faker()

db = Database(
    user="postgres",
    password="...",
    host="localhost",
    database="postgres"
)

engine = db.create_engine()

session = Session(engine)

users = []

for _ in range(20):

    user = User(
        name=fake.name(),
        email=fake.unique.email()
    )

    users.append(user)

    session.add(user)

for user in users:

    address = Address(
        street=fake.street_address(),
        city=fake.city(),
        country=fake.country(),
        user=user
    )

    session.add(address)

brands = [
    "Toyota",
    "Honda",
    "Ford",
    "Hyundai",
    "Nissan"
]

models = [
    "Corolla",
    "Civic",
    "Focus",
    "Elantra",
    "Sentra"
]

for _ in range(30):

    owner = random.choice(
        users + [None]
    )

    car = Car(
        brand=random.choice(brands),
        model=random.choice(models),
        year=random.randint(2005, 2025),
        user=owner
    )

    session.add(car)

    session.commit()