import csv
import os
from student import Student


def export_students_to_csv(students, path="students.csv"):
    """
    Export the list of student objects to a CSV file.

    Parameters:
        students (list): List of Student objects.
        path (str): File path where the CSV will be saved.
    """

    # Validate that there is data to export
    if not students:
        print("\nNo students to export.\n")
        return

    try:
        # Define CSV column headers
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        # Open file in write mode (overwrite existing content)
        with open(path, mode="w", newline="", encoding="utf-8") as file:

            # Create writer object
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Convert each Student object into a dictionary
            writer.writerows([
                {
                    "name": s.name,
                    "section": s.section,
                    "spanish_grade": s.spanish_grade,
                    "english_grade": s.english_grade,
                    "social_studies_grade": s.social_studies_grade,
                    "science_grade": s.science_grade
                }
                for s in students
            ])

        # Success message
        print("-" * 42)
        print(f"\nData successfully exported to {path}\n")
        print("-" * 42)

    except Exception as e:
        # Handle unexpected errors during export
        print(f"Error exporting data: {e}")


def import_students_from_csv(path="students.csv"):
    """
    Import student records from a CSV file and convert them into Student objects.

    Parameters:
        path (str): File path to read the CSV from.

    Returns:
        list: A list of Student objects.
    """

    # Validate file existence
    if not os.path.exists(path):
        print(f"\nFile '{path}' not found.\n")
        return []

    students = []

    try:
        # Open file in read mode
        with open(path, mode="r", encoding="utf-8") as file:

            # Read CSV rows as dictionaries
            reader = csv.DictReader(file)

            for i, row in enumerate(reader, start=1):
                try:
                    # Create Student object from CSV row
                    student = Student(
                        row["name"],
                        row["section"],
                        int(row["spanish_grade"]),
                        int(row["english_grade"]),
                        int(row["social_studies_grade"]),
                        int(row["science_grade"])
                    )

                    # Add object to list
                    students.append(student)

                except KeyError as e:
                    # Handle missing columns
                    print(f"Missing column {e} in row #{i}")

                except ValueError:
                    # Handle invalid data types (e.g., non-numeric grades)
                    print(f"Invalid data format in row #{i}")

        # Success message
        print("-" * 44)
        print(f"\nData successfully imported from {path}\n")
        print("-" * 44)

        return students

    except Exception as e:
        # Handle unexpected errors
        print(f"Error importing data: {e}")
        return []