from datetime import datetime


# Validate that the text field is not empty
def validate_text_input(text):

    # Remove blank spaces from beginning and end
    cleaned_text = text.strip()

    # Check if the text is empty
    if cleaned_text == "":
        raise ValueError("Input cannot be empty")

    return cleaned_text


# Validate that the amount is a valid positive number
def validate_amount(amount):

    try:

        # Convert input to float
        amount = float(amount)

    except ValueError:

        raise ValueError("Amount must be a valid number")

    # Check if amount is greater than zero
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    return amount


# Validate transaction type
def validate_transaction_type(transaction_type):

    valid_types = ["Income", "Expense"]

    # Check if transaction type exists
    if transaction_type not in valid_types:
        raise ValueError("Invalid transaction type")

    return transaction_type


# Validate date format and future dates
def validate_date(date_text):

    try:

        # Convert string to datetime object
        date = datetime.strptime(date_text, "%d/%m/%Y")

    except ValueError:

        raise ValueError("Invalid date format. Use dd/mm/yyyy")

    # Get current date
    current_date = datetime.now()

    # Check if date is in the future
    if date > current_date:
        raise ValueError("Date cannot be in the future")

    return date_text


# Validate that at least one category exists
def validate_categories(categories):

    # Check if categories list is empty
    if len(categories) == 0:
        raise ValueError("No categories available")

    return True