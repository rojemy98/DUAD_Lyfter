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

from services.filters import (
    filter_transactions_by_date
)
from services.validations import (
    validate_date
)

from services.csv_exporter import (
    export_transactions_report
)


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


# Refresh all window data
def refresh_dashboard(window, finance_manager):

    # Build updated expenses data
    expenses_data = build_table_data(
        finance_manager.transactions,
        "Expense"
    )

    # Build updated incomes data
    incomes_data = build_table_data(
        finance_manager.transactions,
        "Income"
    )

    # Update expenses table
    window["-EXPENSES_TABLE-"].update(
        values=expenses_data
    )

    # Update incomes table
    window["-INCOMES_TABLE-"].update(
        values=incomes_data
    )

    # Update totals
    window["-INCOME_TEXT-"].update(
        f"Income: {finance_manager.get_total_income()}"
    )

    window["-EXPENSE_TEXT-"].update(
        f"Expenses: {finance_manager.get_total_expenses()}"
    )

    window["-BALANCE_TEXT-"].update(
        f"Balance: {finance_manager.get_balance()}"
    )


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
            sg.Text("Start Date"),

            sg.Input(
                key="-START_DATE-",
                size=(15, 1)
            ),

            sg.Text("End Date"),

            sg.Input(
                key="-END_DATE-",
                size=(15, 1)
            ),

            sg.Button(
                "Filter",
                size=(12, 1)
            ),

            sg.Button(
                "Clear Filters",
                size=(12, 1)
            )
        ],

        [
            sg.HorizontalSeparator()
        ],

        [
            sg.Text(
                f"Income: {finance_manager.get_total_income()}",
                font=("Arial Bold", 12),
                key="-INCOME_TEXT-"
            ),

            sg.Text(
                " " * 10
            ),

            sg.Text(
                f"Expenses: {finance_manager.get_total_expenses()}",
                font=("Arial Bold", 12),
                key="-EXPENSE_TEXT-"
            ),

            sg.Text(
                " " * 10
            ),

            sg.Text(
                f"Balance: {finance_manager.get_balance()}",
                font=("Arial Bold", 12),
                key="-BALANCE_TEXT-"
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
                "Export CSV",
                size=(15, 1),
                button_color=("white", "#8b008b")
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

            open_add_expense_window(
                finance_manager
            )

            # Refresh dashboard after adding expense
            refresh_dashboard(
                window,
                finance_manager
            )

        # Add income event
        if event == "Add Income":

            open_add_income_window(
                finance_manager
            )

            # Refresh dashboard after adding income
            refresh_dashboard(
                window,
                finance_manager
            )

        # New category event
        if event == "New Category":

            open_add_category_window(finance_manager)

        # Filter transactions event
        if event == "Filter":

            try:

                # Validate dates
                start_date = validate_date(
                    values["-START_DATE-"]
                )

                end_date = validate_date(
                    values["-END_DATE-"]
                )

                # Filter transactions
                filtered_transactions = (
                    filter_transactions_by_date(
                        finance_manager.transactions,
                        start_date,
                        end_date
                    )
                )

                # Build filtered tables
                expenses_data = build_table_data(
                    filtered_transactions,
                    "Expense"
                )

                incomes_data = build_table_data(
                    filtered_transactions,
                    "Income"
                )

                # Update tables
                window["-EXPENSES_TABLE-"].update(
                    values=expenses_data
                )

                window["-INCOMES_TABLE-"].update(
                    values=incomes_data
                )

            except ValueError as error:

                sg.popup_error(error)

        # Clear filters event
        if event == "Clear Filters":

            refresh_dashboard(
                window,
                finance_manager
            )

        # Export CSV event
        if event == "Export CSV":

            file_path = sg.popup_get_file(

                "Save CSV Report",

                save_as=True,

                default_extension=".csv",

                file_types=(
                    ("CSV Files", "*.csv"),
                )
            )

            # Check if user selected path
            if file_path:

                export_transactions_report(
                    finance_manager.transactions,
                    file_path
                )

                sg.popup(
                    "CSV report exported successfully"
                )

    # Close window
    window.close()