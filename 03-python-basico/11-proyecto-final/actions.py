students = []  # Global list to store all student records


def get_valid_grade(subject):
    """
    Prompt the user to enter a valid grade (0–100) for a given subject.
    Continues asking until a valid integer within range is provided.
    """
    while True:
        try:
            grade = int(input(f"Enter {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade  # Return valid grade and exit loop
            else:
                print("Invalid grade. Must be between 0 and 100.")
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please enter a number.")


def get_valid_number(prompt):
    """
    Prompt the user to enter a positive integer.
    Ensures the value is greater than zero.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value  # Return valid number
            else:
                print("Number must be greater than 0.")
        except ValueError:
            # Handle invalid numeric input
            print("Invalid input. Please enter a valid number.")


def get_non_empty_input(prompt):
    """
    Prompt the user to enter a non-empty string.
    Trims whitespace and validates that input is not empty.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value  # Return valid non-empty string
        else:
            print("This field cannot be empty.")


def insert_student():
    """
    Register one or more students by collecting their personal information
    and grades. Stores each student as a dictionary in the global list.
    """
    # Get number of students to register
    n = get_valid_number("Enter the quantity of students you want to register: ")

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        # Collect the student information
        name = get_non_empty_input("Enter the student name: ")
        section = get_non_empty_input("Enter the student section: ")

        # Collect validated grades for each subject
        spanish_grade = get_valid_grade("Spanish")
        english_grade = get_valid_grade("English")
        social_studies_grade = get_valid_grade("Social Studies")
        science_grade = get_valid_grade("Science")

        # Create student record as a dictionary
        new_student = {
            "name": name,
            "section": section,
            "spanish_grade": spanish_grade,
            "english_grade": english_grade,
            "social_studies_grade": social_studies_grade,
            "science_grade": science_grade
        }

        # Add student to the global list
        students.append(new_student)

    # Display confirmation message based on number of students registered
    if n == 1:
        print("\nStudent registered successfully")
    else:
        print("\nStudents registered successfully")


def get_all_students():
    """
    Retrieve and display all student records stored in the global list.
    """

    # Check if the students list is empty
    if not students:
        print("\nNo students registered.\n")
        return  # Exit the function early if no data is available

    print("\n=== Student List ===\n")

    # Iterate through the list of students with an index starting at 1
    for i, student in enumerate(students, start=1):
        try:
            # Display student basic information
            print(f"Student #{i}")
            print(f"Name: {student['name']}")
            print(f"Section: {student['section']}")

            # Display student grades
            print(f"Spanish: {student['spanish_grade']}")
            print(f"English: {student['english_grade']}")
            print(f"Social Studies: {student['social_studies_grade']}")
            print(f"Science: {student['science_grade']}")

            # Print a visual separator between students
            print("-" * 30)

        except KeyError as e:
            # Handle missing keys in the student dictionary
            print(f"Error: Missing data for {e} in student #{i}")
        except Exception as e:
            # Catch any unexpected errors to prevent program crash
            print(f"Unexpected error while displaying student #{i}: {e}")