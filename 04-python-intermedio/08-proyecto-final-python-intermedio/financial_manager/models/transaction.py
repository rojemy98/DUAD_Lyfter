class Transaction:

    def __init__(
        self,
        title,
        amount,
        category,
        transaction_type,
        date
    ):

        self.title = title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = date


    def to_list(self):

        return [
            self.date,
            self.title,
            self.amount,
            self.category,
            self.transaction_type
        ]