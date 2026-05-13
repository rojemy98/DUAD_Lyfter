import FreeSimpleGUI as sg
from gui.add_category_window import (
    open_add_category_window
)
from gui.add_expense_window import (
    open_add_expense_window
)
from gui.add_income_window import (
    open_add_income_window
)

from models.finance_manager import FinanceManager


# Set application theme
sg.theme("DarkBlue3")

# Set global font
sg.set_options(font=("Arial", 12))


# Create finance manager instance
finance_manager = FinanceManager()


# Build table data from transactions
def build_table_data(transactions, transaction_type):

    table_data = []

    # Filter transactions by type
    for transaction in transactions:

        if transaction.transaction_type == transaction_type:

            table_data.append([
                transaction.title,
                transaction.amount,
                transaction.category
            ])

    return table_data


# Create main window
def run_main_window():

    # Define table headers
    table_headers = [
        "Title",
        "Amount",
        "Category"
    ]

    # Build expenses table data
    expenses_data = build_table_data(
        finance_manager.transactions,
        "Expense"
    )

    # Build incomes table data
    incomes_data = build_table_data(
        finance_manager.transactions,
        "Income"
    )

    # Create expenses table
    expenses_table = sg.Table(

        values=expenses_data,

        headings=table_headers,

        justification="center",

        auto_size_columns=True,

        alternating_row_color="#2b475d",

        num_rows=12,

        expand_x=True,

        key="-EXPENSES_TABLE-"
    )

    # Create incomes table
    incomes_table = sg.Table(

        values=incomes_data,

        headings=table_headers,

        justification="center",

        auto_size_columns=True,

        alternating_row_color="#2b475d",

        num_rows=12,

        expand_x=True,

        key="-INCOMES_TABLE-"
    )

    # Create layout
    layout = [

        [
            sg.Text(
                "Personal Finance Manager",
                font=("Arial Bold", 22),
                expand_x=True,
                justification="center"
            )
        ],

        [
            sg.HorizontalSeparator()
        ],

        [
            sg.Text(
                f"Income: {finance_manager.get_total_income()}",
                font=("Arial Bold", 12)
            ),

            sg.Text(
                " " * 10
            ),

            sg.Text(
                f"Expenses: {finance_manager.get_total_expenses()}",
                font=("Arial Bold", 12)
            ),

            sg.Text(
                " " * 10
            ),

            sg.Text(
                f"Balance: {finance_manager.get_balance()}",
                font=("Arial Bold", 12)
            )
        ],

        [
            sg.HorizontalSeparator()
        ],

        [
            sg.Button(
                "Add Expense",
                size=(15, 1),
                button_color=("white", "#b22222")
            ),

            sg.Button(
                "Add Income",
                size=(15, 1),
                button_color=("white", "#228b22")
            ),

            sg.Button(
                "New Category",
                size=(15, 1),
                button_color=("white", "#1e90ff")
            ),

            sg.Button(
                "Exit",
                size=(15, 1)
            )
        ],

        [
            sg.HorizontalSeparator()
        ],

        [
            sg.Frame(

                "Expenses",

                [
                    [expenses_table]
                ],

                expand_x=True,

                pad=(10, 10)
            ),

            sg.Frame(

                "Incomes",

                [
                    [incomes_table]
                ],

                expand_x=True,

                pad=(10, 10)
            )
        ]
    ]

    # Create window
    window = sg.Window(

        "Personal Finance Manager",

        layout,

        size=(1200, 600),

        finalize=True,

        resizable=True
    )

    # Main event loop
    while True:

        event, values = window.read()

        # Close application
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        # Add expense event
        if event == "Add Expense":

            open_add_expense_window(finance_manager)

        # Add income event
        if event == "Add Income":

            open_add_income_window(finance_manager)

        # New category event
        if event == "New Category":

            open_add_category_window(finance_manager)

    # Close window
    window.close()