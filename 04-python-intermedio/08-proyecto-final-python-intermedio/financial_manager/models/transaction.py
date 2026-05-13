class Transaction:

    # Initialize a financial transaction
    def __init__(
        self,
        title,
        amount,
        category,
        transaction_type,
        date
    ):

        # Title of the transaction
        self.title = title

        # Value of the transaction
        self.amount = amount

        # Category assigned to the transaction
        self.category = category

        # Type of transaction: Income or Expense
        self.transaction_type = transaction_type

        # Date of the transaction (format: dd/mm/yyyy)
        self.date = date


    # Convert transaction object into a list
    def to_list(self):

        return [
            self.date,               # Transaction date
            self.title,              # Transaction title
            self.amount,             # Transaction amount
            self.category,           # Transaction category
            self.transaction_type    # Income or Expense type
        ]