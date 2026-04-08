import menu


def main():
    """
    Entry point of the application.
    """

    # Initialize the main data structure to store student records
    students = []

    # Start the menu loop, passing the students list as state
    menu.display_menu(students)


if __name__ == "__main__":
    main()