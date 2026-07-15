"""
Database health check script.

This script verifies:

1. Database connectivity.
2. Required tables exist.
3. At least one car is available.

If every validation succeeds, the script prints:

    DB OK. System operating normally.

Otherwise, it prints an error message describing the problem.
"""

import sys

from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from db import PgManager


# Database configuration
db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Nyjah2022_",
    host="localhost"
)


REQUIRED_TABLES = [
    "users",
    "cars",
    "rentals"
]


def table_exists(table_name):
    """
    Check whether a table exists.

    Args:
        table_name (str): Table name.

    Returns:
        bool
    """

    query = """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema = 'lyfter_car_rental'
            AND table_name = %s
        );
    """

    result = db_manager.execute_query(
        query,
        table_name
    )

    return result[0][0]


def available_cars():
    """
    Return the number of available cars.

    Returns:
        int
    """

    query = """
        SELECT COUNT(*)
        FROM lyfter_car_rental.cars
        WHERE status = 'Available';
    """

    result = db_manager.execute_query(query)

    return result[0][0]


def health_check():
    """
    Execute every system validation.
    """

    try:

        # Validate database connection
        db_manager.execute_query("SELECT 1;")

        # Validate required tables
        for table in REQUIRED_TABLES:

            if not table_exists(table):

                print(f"DB ERROR. Table '{table}' does not exist.")

                return

        # Validate available cars
        if available_cars() == 0:

            print("DB ERROR. No available cars.")

            return

        print("DB OK. System operating normally.")

    except Exception as error:

        print(f"DB ERROR. {error}")


if __name__ == "__main__":
    health_check()