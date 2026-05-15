import csv
import os

from models.category import Category
from models.transaction import Transaction


# Save categories into CSV file
def save_categories(categories):

    # Create data directory if it not exist
    os.makedirs("data", exist_ok=True)

    # Open CSV file in write mode
    with open(
        "data/categories.csv",
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write CSV headers
        writer.writerow([
            "name",
            "color"
        ])

        # Write category rows
        for category in categories:

            writer.writerow(
                category.to_list()
            )


# Load categories from CSV file
def load_categories():

    categories = []

    # Check if file exists
    if not os.path.exists("data/categories.csv"):
        return categories

    # Open CSV file in read mode
    with open(
        "data/categories.csv",
        mode="r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        # Convert each row into a Category object
        for row in reader:

            category = Category(
                row["name"],
                row["color"]
            )

            categories.append(category)

    return categories


# Save transactions into CSV file
def save_transactions(transactions):

    # Create data directory if it does not exist
    os.makedirs("data", exist_ok=True)

    # Open CSV file in write mode
    with open(
        "data/transactions.csv",
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write CSV headers
        writer.writerow([
            "date",
            "title",
            "amount",
            "category",
            "transaction_type"
        ])

        # Write transaction rows
        for transaction in transactions:

            writer.writerow(
                transaction.to_list()
            )


# Load transactions from CSV file
def load_transactions():

    transactions = []

    # Check if file exists
    if not os.path.exists("data/transactions.csv"):
        return transactions

    # Open CSV file in read mode
    with open(
        "data/transactions.csv",
        mode="r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        # Convert each row into a Transaction object
        for row in reader:

            transaction = Transaction(
                row["title"],
                float(row["amount"]),
                row["category"],
                row["transaction_type"],
                row["date"]
            )

            transactions.append(transaction)

    return transactions