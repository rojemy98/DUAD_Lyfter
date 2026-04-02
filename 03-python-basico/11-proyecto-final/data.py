import csv
import os


def export_students_to_csv(students, path="students.csv"):
    """
    Export the list of student records to a CSV file.
    """

    # Validate that there is data to export
    if not students:
        print("\nNo students to export.\n")
        return

    try:
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        # Open file in write mode
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("-" * 42)
        print(f"\nData successfully exported to {path}\n")
        print("-" * 42)

    except Exception as e:
        print(f"Error exporting data: {e}")


def import_students_from_csv(path="students.csv"):
    """
    Import student records from a CSV file.
    Returns a new list of students.
    """

    if not os.path.exists(path):
        print(f"\nFile '{path}' not found.\n")
        return []

    students = []

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader, start=1):
                try:
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish_grade": int(row["spanish_grade"]),
                        "english_grade": int(row["english_grade"]),
                        "social_studies_grade": int(row["social_studies_grade"]),
                        "science_grade": int(row["science_grade"])
                    }

                    students.append(student)

                except KeyError as e:
                    print(f"Missing column {e} in row #{i}")
                except ValueError:
                    print(f"Invalid data format in row #{i}")

        print("-" * 44)
        print(f"\nData successfully imported from {path}\n")
        print("-" * 44)

        return students

    except Exception as e:
        print(f"Error importing data: {e}")
        return []