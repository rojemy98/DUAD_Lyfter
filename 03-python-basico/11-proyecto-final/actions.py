import re


def get_valid_grade(subject):
    """
    Ask the user for a grade between 0 and 100.
    Keeps asking until a valid integer is entered.
    """
    while True:
        try:
            grade = int(input(f"Enter {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Invalid grade. Must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_number(prompt):
    """
    Ask the user for a positive integer (> 0).
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
    Ask for a valid name (no numbers, not empty).
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
    Ask for a valid section (e.g., 10A, 8B).
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
    """
    return any(
        s["name"].lower() == name.lower() and
        s["section"].lower() == section.lower()
        for s in students
    )


def insert_students(students):
    """
    Add new students to the list and return updated list.
    """
    n = get_valid_number("Enter number of students: ")

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        name = get_valid_name("Enter name: ")
        section = get_valid_section("Enter section: ")

        while student_exists(students, name, section):
            print("Student already exists.")
            name = get_valid_name("Enter name: ")
            section = get_valid_section("Enter section: ")

        new_student = {
            "name": name,
            "section": section,
            "spanish_grade": get_valid_grade("Spanish"),
            "english_grade": get_valid_grade("English"),
            "social_studies_grade": get_valid_grade("Social Studies"),
            "science_grade": get_valid_grade("Science"),
        }

        students.append(new_student)

    print("\nStudents registered successfully.\n")
    return students


def get_all_students(students):
    """
    Print all students in the list.
    """
    if not students:
        print("\nNo students registered.\n")
        return

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
    Calculate student's average grade.
    """
    return (
        student["spanish_grade"] +
        student["english_grade"] +
        student["social_studies_grade"] +
        student["science_grade"]
    ) / 4


def get_top3_average_grades(students):
    """
    Show top 3 students based on average grade.
    """
    if not students:
        print("\nNo students registered.\n")
        return

    top3 = sorted(students, key=get_average, reverse=True)[:3]

    print("\n=== Top 3 Students ===\n")
    for i, s in enumerate(top3, 1):
        print(f"#{i} {s['name']} - Avg: {get_average(s):.2f}")


def get_students_overall_average(students):
    """
    Calculate overall average (average of all students' averages).
    """
    if not students:
        print("\nNo students registered.\n")
        return

    averages = [get_average(s) for s in students]
    overall = sum(averages) / len(averages)

    print(f"\nOverall average: {overall:.2f}\n")


def delete_student(students):
    """
    Remove a student from the list.
    """
    if not students:
        print("\nNo students registered.\n")
        return students

    name = input("Enter name: ").strip()
    section = input("Enter section: ").strip()

    for i, s in enumerate(students):
        if s["name"].lower() == name.lower() and s["section"].lower() == section.lower():
            confirm = input(f"Delete {s['name']}? (y/n): ").lower()
            if confirm == "y":
                students.pop(i)
                print("Student deleted.\n")
            return students

    print("Student not found.\n")
    return students


def get_failed_students(students):
    """
    Show students with at least one failed subject (<60).
    """
    if not students:
        print("\nNo students registered.\n")
        return

    print("\n=== Failed Students ===\n")
    found = False

    for s in students:
        failed = {
            k: v for k, v in {
                "Spanish": s["spanish_grade"],
                "English": s["english_grade"],
                "Social Studies": s["social_studies_grade"],
                "Science": s["science_grade"]
            }.items() if v < 60
        }

        if failed:
            found = True
            print(f"{s['name']} ({s['section']})")
            for subject, grade in failed.items():
                print(f" - {subject}: {grade}")
            print("-" * 30)

    if not found:
        print("No failed students.\n")