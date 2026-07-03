"""
Database seed script.

This script populates the database with fake data using Faker.

It creates:

- 200 users
- 100 cars
- Between 50 and 150 rentals
"""

import random
import sys
from pathlib import Path

from faker import Faker

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from db import PgManager

from repositories import (
    UserRepository,
    CarRepository,
    RentalRepository
)

fake = Faker()


# Database configuration
db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Nyjah2022_",
    host="localhost"
)

users_repo = UserRepository(db_manager)
cars_repo = CarRepository(db_manager)
rentals_repo = RentalRepository(db_manager)


# Available brands and models
CAR_CATALOG = {
    "Toyota": [
        "Corolla",
        "Yaris",
        "RAV4",
        "Hilux"
    ],
    "Honda": [
        "Civic",
        "Accord",
        "CR-V"
    ],
    "Nissan": [
        "Sentra",
        "Versa",
        "X-Trail"
    ],
    "Ford": [
        "Escape",
        "Focus",
        "Explorer"
    ],
    "BMW": [
        "320i",
        "X3",
        "X5"
    ],
    "Audi": [
        "A3",
        "A4",
        "Q5"
    ],
    "Mazda": [
        "CX-5",
        "Mazda3",
        "Mazda6"
    ],
    "Hyundai": [
        "Elantra",
        "Tucson",
        "Santa Fe"
    ],
    "Kia": [
        "Rio",
        "Sportage",
        "Sorento"
    ],
    "Chevrolet": [
        "Spark",
        "Cruze",
        "Tracker"
    ]
}


def generate_users(total=200):
    """
    Generate fake users.

    Returns:
        list
    """

    users = []

    for _ in range(total):

        first_name = fake.first_name()
        last_name = fake.last_name()

        username = (
            first_name.lower()
            + str(random.randint(100, 999))
        )

        users.append(
            (
                first_name,
                last_name,
                username,
                fake.unique.email(),
                "Password123!",
                fake.date_of_birth(
                    minimum_age=18,
                    maximum_age=70
                ),
                random.choices(
                    ["Active", "Inactive"],
                    weights=[90, 10]
                )[0]
            )
        )

    return users


def insert_users(users):
    """
    Insert users into the database.
    """

    query = """
        INSERT INTO lyfter_car_rental.users
        (
            name,
            last_name,
            username,
            email,
            password,
            birthdate,
            status
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        );
    """

    for user in users:
        db_manager.execute_query(
            query,
            *user
        )

    db_manager.commit()

    print(f"{len(users)} users created.")

def generate_cars(total=100):
    """
    Generate fake cars.

    Args:
        total (int): Number of cars to generate.

    Returns:
        list
    """

    cars = []

    brands = list(CAR_CATALOG.keys())

    for _ in range(total):

        brand = random.choice(brands)

        model = random.choice(CAR_CATALOG[brand])

        year = random.randint(2010, 2025)

        cars.append(
            (
                brand,
                model,
                year,
                "Available"
            )
        )

    return cars

def generate_rentals():
    """
    Generate random rental history.

    Returns:
        int
    """

    active_users = users_repo.get_active_user_ids()

    available_cars = cars_repo.get_available_car_ids()

    if not active_users or not available_cars:

        print("Unable to generate rentals.")

        return 0

    total_rentals = random.randint(
        50,
        min(
            150,
            len(available_cars)
        )
    )

    rentals_created = 0

    random.shuffle(active_users)
    random.shuffle(available_cars)

    for car_id in available_cars[:total_rentals]:

        user_id = random.choice(active_users)

        rental = {
            "user_id": user_id,
            "car_id": car_id
        }

        created = rentals_repo.create_rental(rental)

        if created:
            rentals_created += 1

    return rentals_created

def main():
    """
    Seed the database.
    """

    print("\nGenerating fake users...")

    users = generate_users(200)

    users_repo.bulk_create_users(users)

    print("200 users inserted.")

    print("\nGenerating fake cars...")

    cars = generate_cars(100)

    cars_repo.bulk_create_cars(cars)

    print("100 cars inserted.")

    print("\nGenerating rental history...")

    rentals = generate_rentals()

    print(f"{rentals} rentals inserted.")

    print("\nDatabase successfully populated.")


if __name__ == "__main__":

    main()

    db_manager.close_connection()