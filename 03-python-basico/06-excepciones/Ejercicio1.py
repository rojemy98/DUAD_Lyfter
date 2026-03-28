def addition(actual_number):

    try:
        num2 = int(input(f"Enter a number to sum => {actual_number} + : "))
        result = actual_number + num2
        return result

    except ValueError:
        print("Please enter a valid number")
        return actual_number


def subtraction(actual_number):

    try:
        num2 = float(input(f"Enter a number for subtraction => {actual_number} - : "))
        result = actual_number - num2
        return result

    except ValueError:
        print("Please enter a valid number")
        return actual_number


def multiplication(actual_number):

    try:
        num2 = float(input(f"Enter a number for multiplication => {actual_number} x : "))
        result = actual_number * num2
        return result

    except ValueError:
        print("Please enter a valid number")
        return actual_number


def division(actual_number):

    try:
        num2 = float(input(f"Enter a number for division => {actual_number} / : "))

        if num2 == 0:
            print("You cannot divide by zero")
            return actual_number

        result = actual_number / num2
        return result

    except ValueError:
        print("Please enter a valid number")
        return actual_number


def delete_result():
    return 0


def main():
    actual_number = 0

    while True:

        print("\n*** Calculator ***")
        print(f"Current result: {actual_number}")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Delete results")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == "1":
            actual_number = addition(actual_number)

        elif option == "2":
            actual_number = subtraction(actual_number)

        elif option == "3":
            actual_number = multiplication(actual_number)

        elif option == "4":
            actual_number = division(actual_number)

        elif option == "5":
            actual_number = delete_result()

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()