from services.persistence import (
    save_categories,
    save_transactions,
    load_categories,
    load_transactions
)


class FinanceManager:

    # Initialize the finance manager and load persisted data
    def __init__(self):

        # Load saved categories from CSV
        self.categories = load_categories()

        # Load saved transactions from CSV
        self.transactions = load_transactions()


    # Add a new category and persist the updated list
    def add_category(self, category):

        # Store category in memory
        self.categories.append(category)

        # Persist categories to CSV
        save_categories(self.categories)


    # Add a new transaction and persist the updated list
    def add_transaction(self, transaction):

        # Store transaction in memory
        self.transactions.append(transaction)

        # Persist transactions to CSV
        save_transactions(self.transactions)


    # Calculate total income from all transactions
    def get_total_income(self):

        total_income = 0

        # Iterate through all transactions
        for transaction in self.transactions:

            # Only consider income transactions
            if transaction.transaction_type == "Income":

                total_income += transaction.amount

        return total_income


    # Calculate total expenses from all transactions
    def get_total_expenses(self):

        total_expenses = 0

        # Iterate through all transactions
        for transaction in self.transactions:

            # Only consider expense transactions
            if transaction.transaction_type == "Expense":

                total_expenses += transaction.amount

        return total_expenses


    # Calculate net balance (income - expenses)
    def get_balance(self):

        return self.get_total_income() - self.get_total_expenses()