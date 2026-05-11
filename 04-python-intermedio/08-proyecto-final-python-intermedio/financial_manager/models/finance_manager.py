class FinanceManager:

    def __init__(self):

        self.categories = []
        self.transactions = []


    def add_category(self, category):

        self.categories.append(category)


    def add_transaction(self, transaction):

        self.transactions.append(transaction)


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