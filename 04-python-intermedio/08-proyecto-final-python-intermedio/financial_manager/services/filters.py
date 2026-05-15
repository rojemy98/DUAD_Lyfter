from datetime import datetime


# Filter transactions by date range
def filter_transactions_by_date(
    transactions,
    start_date,
    end_date
):

    filtered_transactions = []

    # Convert string dates into datetime objects
    start_date = datetime.strptime(
        start_date,
        "%d/%m/%Y"
    )

    end_date = datetime.strptime(
        end_date,
        "%d/%m/%Y"
    )

    # Iterate through all transactions
    for transaction in transactions:

        transaction_date = datetime.strptime(
            transaction.date,
            "%d/%m/%Y"
        )

        # Check if transaction is inside range
        if start_date <= transaction_date <= end_date:

            filtered_transactions.append(
                transaction
            )

    return filtered_transactions