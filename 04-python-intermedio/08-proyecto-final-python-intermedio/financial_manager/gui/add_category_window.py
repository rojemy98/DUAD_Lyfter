import FreeSimpleGUI as sg

from models.category import Category

from services.validations import (
    validate_text_input
)


# Open add category window
def open_add_category_window(finance_manager):

    # Create window layout
    layout = [

        [
            sg.Text("Category Name")
        ],

        [
            sg.Input(
                key="-CATEGORY_NAME-",
                size=(30, 1)
            )
        ],

        [
            sg.Text("Category Color")
        ],

        [
            sg.Input(
                default_text="#FFFFFF",
                key="-CATEGORY_COLOR-",
                size=(30, 1)
            ),

            sg.ColorChooserButton(
                "Choose Color",
                target="-CATEGORY_COLOR-"
            )
        ],

        [
            sg.Button("Save"),

            sg.Button("Cancel")
        ]
    ]

    # Create window
    window = sg.Window(
        "Add Category",
        layout,
        modal=True
    )

    # Event loop
    while True:

        event, values = window.read()

        # Close window
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        # Save category event
        if event == "Save":

            try:

                # Validate category name
                category_name = validate_text_input(
                    values["-CATEGORY_NAME-"]
                )

                # Get selected color
                category_color = values["-CATEGORY_COLOR-"]

                # Create category object
                category = Category(
                    category_name,
                    category_color
                )

                # Add category into finance manager
                finance_manager.add_category(category)

                # Success popup
                sg.popup(
                    "Category created successfully"
                )

                break

            except ValueError as error:

                # Show validation error
                sg.popup_error(error)

    # Close window
    window.close()