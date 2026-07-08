"""
Database backup script.

This script exports the contents of the users, cars and rentals
tables into CSV files.

Each execution generates three files inside the db_backups folder.

Example:

db_backups/
    users_2026-06-27.csv
    cars_2026-06-27.csv
    rentals_2026-06-27.csv
"""

import csv
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


def export_table(table_name, columns):
    """
    Export a database table into a CSV file.

    Args:
        table_name (str): Database table name.
        columns (list): List of column names.
    """

    query = f"""
        SELECT {", ".join(columns)}
        FROM lyfter_car_rental.{table_name};
    """

    results = db_manager.execute_query(query)

    backup_directory = Path("db_backups")
    backup_directory.mkdir(exist_ok=True)

    current_date = datetime.now().strftime("%Y-%m-%d")

    file_path = backup_directory / f"{table_name}_{current_date}.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(columns)

        writer.writerows(results)

    print(f"Backup created: {file_path}")


def main():
    """
    Export all application tables.
    """

    export_table(
        "users",
        [
            "id",
            "name",
            "last_name",
            "username",
            "email",
            "birthdate",
            "status"
        ]
    )

    export_table(
        "cars",
        [
            "id",
            "brand",
            "model",
            "manufacturing_year",
            "status"
        ]
    )

    export_table(
        "rentals",
        [
            "id",
            "user_id",
            "car_id",
            "rental_date",
            "rental_status"
        ]
    )

    print("\nDatabase backup completed successfully.")


if __name__ == "__main__":
    main()