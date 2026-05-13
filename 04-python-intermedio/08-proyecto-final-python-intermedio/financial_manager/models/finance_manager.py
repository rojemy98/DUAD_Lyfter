from services.persistence import (
    save_categories,
    save_transactions,
    load_categories,
    load_transactions
)

class FinanceManager:

    def __init__(self):

        # Load saved categories
        self.categories = load_categories()

        # Load saved transactions
        self.transactions = load_transactions()


    def add_category(self, category):

        # Add category into memory
        self.categories.append(category)

        # Save updated categories
        save_categories(self.categories)


    def add_transaction(self, transaction):

        # Add transaction into memory
        self.transactions.append(transaction)

        # Save updated transactions
        save_transactions(self.transactions)


    def get_total_income(self):

        total_income = 0

        for transaction in self.transactions:

            if transaction.transaction_type == "Income":

                total_income += transaction.amount

        return total_income


    def get_total_expenses(self):

        total_expenses = 0

        for transaction in self.transactions:

            if transaction.transaction_type == "Expense":

                total_expenses += transaction.amount

        return total_expenses


    def get_balance(self):

        return self.get_total_income() - self.get_total_expenses()