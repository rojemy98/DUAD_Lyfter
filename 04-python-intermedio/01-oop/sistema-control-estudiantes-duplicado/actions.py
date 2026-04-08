import re
from student import Student


def get_valid_grade(subject):
    """
    Prompt the user to enter a valid grade for a given subject.
    The grade must be an integer between 0 and 100.
    Keeps asking until valid input is provided.
    """
    while True:
        try:
            # Convert input to integer
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

            if value > 0:
                return value

            print("Number must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_name(prompt):
    """
    Prompt the user to enter a valid name.
    The name must not be empty and cannot contain numbers.
    """
    while True:
        name = input(prompt).strip()

        if not name:
            print("This field cannot be empty.")

        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")

        else:
            return name


def get_valid_section(prompt):
    """
    Prompt the user to enter a valid section.
    Expected format: digits followed by an uppercase letter (e.g., 10A, 8B).
    """
    pattern = r"^\d+[A-Z]$"

    while True:
        section = input(prompt).strip().upper()

        if not section:
            print("This field cannot be empty.")

        elif not re.match(pattern, section):
            print("Invalid format. Use format like 10A, 8B.")

        else:
            return section


def student_exists(students, name, section):
    """
    Check if a student already exists in the list.
    A student is considered existing if both name and section match (case-insensitive).
    """
    return any(
        s.name.lower() == name.lower() and
        s.section.lower() == section.lower()
        for s in students
    )


def insert_students(students):
    """
    Add new students to the list.
    Prompts the user for student data and appends Student objects.
    """
    n = get_valid_number("Enter number of students: ")

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        # Collect student information
        name = get_valid_name("Enter name: ")
        section = get_valid_section("Enter section: ")

        # Prevent duplicates
        while student_exists(students, name, section):
            print("Student already exists.")
            name = get_valid_name("Enter name: ")
            section = get_valid_section("Enter section: ")

        # Create Student object
        new_student = Student(
            name,
            section,
            get_valid_grade("Spanish"),
            get_valid_grade("English"),
            get_valid_grade("Social Studies"),
            get_valid_grade("Science"),
        )

        # Add to list
        students.append(new_student)

    print("\nStudents registered successfully.\n")
    return students


def get_all_students(students):
    """
    Display all registered students and their grades.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    for i, s in enumerate(students, 1):
        print(f"\nStudent #{i}")
        print(f"Name: {s.name}")
        print(f"Section: {s.section}")
        print(f"Spanish: {s.spanish_grade}")
        print(f"English: {s.english_grade}")
        print(f"Social Studies: {s.social_studies_grade}")
        print(f"Science: {s.science_grade}")
        print("-" * 30)


def get_average(student):
    """
    Calculate and return the average grade of a student.
    """
    return (
        student.spanish_grade +
        student.english_grade +
        student.social_studies_grade +
        student.science_grade
    ) / 4


def get_top3_average_grades(students):
    """
    Display the top 3 students based on their average grade.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    # Sort students by average (descending)
    top3 = sorted(students, key=get_average, reverse=True)[:3]

    print("\n=== Top 3 Students ===\n")

    for i, s in enumerate(top3, 1):
        print(f"#{i} {s.name} - Avg: {get_average(s):.2f}")


def get_students_overall_average(students):
    """
    Calculate and display the overall average grade.
    This represents the average of all students' averages.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    # Compute each student's average
    averages = [get_average(s) for s in students]

    # Compute overall average
    overall = sum(averages) / len(averages)

    print(f"\nOverall average: {overall:.2f}\n")


def delete_student(students):
    """
    Remove a student from the list based on name and section.
    Returns the updated list.
    """
    if not students:
        print("\nNo students registered.\n")
        return students

    name = input("Enter name: ").strip()
    section = input("Enter section: ").strip()

    for i, s in enumerate(students):

        # Match student (case-insensitive)
        if s.name.lower() == name.lower() and s.section.lower() == section.lower():

            # Confirm deletion
            confirm = input(f"Delete {s.name}? (y/n): ").lower()

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

    for s in students:

        # Map subjects to grades
        subjects = {
            "Spanish": s.spanish_grade,
            "English": s.english_grade,
            "Social Studies": s.social_studies_grade,
            "Science": s.science_grade
        }

        # Filter failed subjects
        failed = {k: v for k, v in subjects.items() if v < 60}

        if failed:
            found = True
            print(f"{s.name} ({s.section})")

            for subject, grade in failed.items():
                print(f" - {subject}: {grade}")

            print("-" * 30)

    if not found:
        print("No failed students.\n")