from datetime import datetime

import FreeSimpleGUI as sg

from models.transaction import Transaction

from services.validations import (
    validate_text_input,
    validate_amount,
    validate_date,
    validate_categories
)


# Open add income window
def open_add_income_window(finance_manager):

    try:

        # Validate that categories exist
        validate_categories(
            finance_manager.categories
        )

    except ValueError as error:

        sg.popup_error(error)

        return

    # Build category names list
    category_names = []

    for category in finance_manager.categories:

        category_names.append(
            category.name
        )

    # Get current date
    current_date = datetime.now().strftime("%d/%m/%Y")

    # Create window layout
    layout = [

        [
            sg.Text("Title")
        ],

        [
            sg.Input(
                key="-TITLE-",
                size=(30, 1)
            )
        ],

        [
            sg.Text("Amount")
        ],

        [
            sg.Input(
                key="-AMOUNT-",
                size=(30, 1)
            )
        ],

        [
            sg.Text("Category")
        ],

        [
            sg.Combo(
                values=category_names,
                readonly=True,
                key="-CATEGORY-",
                size=(28, 1)
            )
        ],

        [
            sg.Text("Date")
        ],

        [
            sg.Input(
                default_text=current_date,
                key="-DATE-",
                size=(30, 1)
            )
        ],

        [
            sg.Button("Save"),

            sg.Button("Cancel")
        ]
    ]

    # Create window
    window = sg.Window(
        "Add Income",
        layout,
        modal=True
    )

    # Event loop
    while True:

        event, values = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        # Save income event
        if event == "Save":

            try:

                # Validate title
                title = validate_text_input(
                    values["-TITLE-"]
                )

                # Validate amount
                amount = validate_amount(
                    values["-AMOUNT-"]
                )

                # Validate date
                date = validate_date(
                    values["-DATE-"]
                )

                # Get selected category
                category = values["-CATEGORY-"]

                # Validate category selection
                if category == "":
                    raise ValueError(
                        "Please select a category"
                    )

                # Create income transaction
                transaction = Transaction(
                    title,
                    amount,
                    category,
                    "Income",
                    date
                )

                # Add transaction
                finance_manager.add_transaction(
                    transaction
                )

                # Show success popup
                sg.popup(
                    "Income added successfully"
                )

                break

            except ValueError as error:

                # Show validation error
                sg.popup_error(error)

    # Close window
    window.close()