import re


def get_valid_grade(subject):
    """
    Prompt the user to enter a valid grade for a given subject.
    The grade must be an integer between 0 and 100.
    Keeps asking until valid input is provided.
    """
    while True:
        try:
            # Read input and convert to integer
            grade = int(input(f"Enter {subject} grade (0-100): "))

            # Validate range
            if 0 <= grade <= 100:
                return grade

            print("Invalid grade. Must be between 0 and 100.")

        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number.")


def get_valid_number(prompt):
    """
    Prompt the user to enter a positive integer (> 0).
    Keeps asking until a valid value is entered.
    """
    while True:
        try:
            value = int(input(prompt))

            # Ensure value is greater than zero
            if value > 0:
                return value

            print("Number must be greater than 0.")

        except ValueError:
            # Handle invalid numeric input
            print("Invalid input. Please enter a valid number.")


def get_valid_name(prompt):
    """
    Prompt the user to enter a valid name.
    The name must not be empty and cannot contain numeric characters.
    """
    while True:
        # Read input and remove extra spaces
        name = input(prompt).strip()

        # Validate empty input
        if not name:
            print("This field cannot be empty.")

        # Validate no digits in name
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")

        else:
            return name  # Valid name


def get_valid_section(prompt):
    """
    Prompt the user to enter a valid section.
    Expected format: one or more digits followed by an uppercase letter (e.g., 10A, 8B).
    """
    pattern = r"^\d+[A-Z]$"  # Regex pattern for section validation

    while True:
        # Normalize input
        section = input(prompt).strip().upper()

        # Validate empty input
        if not section:
            print("This field cannot be empty.")

        # Validate format using regex
        elif not re.match(pattern, section):
            print("Invalid format. Use format like 10A, 8B.")

        else:
            return section  # Valid section


def student_exists(students, name, section):
    """
    Check if a student already exists in the list.
    A student is considered existing if both name and section match (case-insensitive).
    """
    return any(
        s["name"].lower() == name.lower() and
        s["section"].lower() == section.lower()
        for s in students
    )


def insert_students(students):
    """
    Add new students to the list.
    Prompts the user for student data and appends it to the list.
    Returns the updated students list.
    """
    # Ask for number of students to register
    n = get_valid_number("Enter number of students: ")

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        # Collect validated student information
        name = get_valid_name("Enter name: ")
        section = get_valid_section("Enter section: ")

        # Ensure no duplicate student
        while student_exists(students, name, section):
            print("Student already exists.")
            name = get_valid_name("Enter name: ")
            section = get_valid_section("Enter section: ")

        # Create student record
        new_student = {
            "name": name,
            "section": section,
            "spanish_grade": get_valid_grade("Spanish"),
            "english_grade": get_valid_grade("English"),
            "social_studies_grade": get_valid_grade("Social Studies"),
            "science_grade": get_valid_grade("Science"),
        }

        # Add student to the list
        students.append(new_student)

    print("\nStudents registered successfully.\n")
    return students


def get_all_students(students):
    """
    Display all registered students and their grades.
    """
    # Check if the list is empty
    if not students:
        print("\nNo students registered.\n")
        return

    # Iterate and display student information
    for i, s in enumerate(students, 1):
        print(f"\nStudent #{i}")
        print(f"Name: {s['name']}")
        print(f"Section: {s['section']}")
        print(f"Spanish: {s['spanish_grade']}")
        print(f"English: {s['english_grade']}")
        print(f"Social Studies: {s['social_studies_grade']}")
        print(f"Science: {s['science_grade']}")
        print("-" * 30)


def get_average(student):
    """
    Calculate and return the average grade of a student.
    """
    return (
        student["spanish_grade"] +
        student["english_grade"] +
        student["social_studies_grade"] +
        student["science_grade"]
    ) / 4


def get_top3_average_grades(students):
    """
    Display the top 3 students based on their average grade.
    """
    # Validate data availability
    if not students:
        print("\nNo students registered.\n")
        return

    # Sort students by average grade (descending)
    top3 = sorted(students, key=get_average, reverse=True)[:3]

    print("\n=== Top 3 Students ===\n")

    # Display results
    for i, s in enumerate(top3, 1):
        print(f"#{i} {s['name']} - Avg: {get_average(s):.2f}")


def get_students_overall_average(students):
    """
    Calculate and display the overall average grade.
    This is the average of all students' individual averages.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    # Compute average for each student
    averages = [get_average(s) for s in students]

    # Compute overall average
    overall = sum(averages) / len(averages)

    print(f"\nOverall average: {overall:.2f}\n")


def delete_student(students):
    """
    Remove a student from the list based on name and section.
    Returns the updated students list.
    """
    if not students:
        print("\nNo students registered.\n")
        return students

    # Get user input
    name = input("Enter name: ").strip()
    section = input("Enter section: ").strip()

    # Search for the student
    for i, s in enumerate(students):

        # Match student (case-insensitive)
        if s["name"].lower() == name.lower() and s["section"].lower() == section.lower():

            # Confirm deletion
            confirm = input(f"Delete {s['name']}? (y/n): ").lower()

            if confirm == "y":
                students.pop(i)
                print("Student deleted.\n")

            return students

    print("Student not found.\n")
    return students


def get_failed_students(students):
    """
    Display students who have failed at least one subject.
    A subject is considered failed if the grade is below 60.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    print("\n=== Failed Students ===\n")
    found = False

    # Iterate through students
    for s in students:

        # Map subjects to grades
        subjects = {
            "Spanish": s["spanish_grade"],
            "English": s["english_grade"],
            "Social Studies": s["social_studies_grade"],
            "Science": s["science_grade"]
        }

        # Filter failed subjects
        failed = {k: v for k, v in subjects.items() if v < 60}

        # If any subject is failed
        if failed:
            found = True
            print(f"{s['name']} ({s['section']})")

            for subject, grade in failed.items():
                print(f" - {subject}: {grade}")

            print("-" * 30)

    # If no failed students found
    if not found:
        print("No failed students.\n")