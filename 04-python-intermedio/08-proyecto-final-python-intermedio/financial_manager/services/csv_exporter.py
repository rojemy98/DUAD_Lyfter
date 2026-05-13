import csv


# Export transactions into report CSV
def export_transactions_report(
    transactions,
    file_path
):

    total_income = 0

    total_expenses = 0

    # Open CSV file
    with open(
        file_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write headers
        writer.writerow([
            "Date",
            "Title",
            "Amount",
            "Category",
            "Type"
        ])

        # Write transaction rows
        for transaction in transactions:

            writer.writerow([
                transaction.date,
                transaction.title,
                transaction.amount,
                transaction.category,
                transaction.transaction_type
            ])

            # Calculate totals
            if transaction.transaction_type == "Income":

                total_income += transaction.amount

            else:

                total_expenses += transaction.amount

        # Write totals section
        writer.writerow([])

        writer.writerow(["Totals"])

        writer.writerow([
            "Total Income",
            total_income
        ])

        writer.writerow([
            "Total Expenses",
            total_expenses
        ])

        writer.writerow([
            "Balance",
            total_income - total_expenses
        ])