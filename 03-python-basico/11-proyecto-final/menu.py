import actions

def display_menu():
    while True:

        print("\n=== Student Management System ===\n")
        print("1. Add new student")
        print("2. List all students")
        print("3. Top 3 - Highest averages")
        print("4. View overall average grade of all students")
        print("5. Export data to CSV")
        print("6. Import data from a CSV (previously exported)")
        print("7. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            actions.insert_student()

        elif option == "2":
            actions.get_all_students()

        elif option == "3":
            actions.get_top3_average_grades()

        elif option == "4":
            actions.get_students_overall_average()

        elif option == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option")
