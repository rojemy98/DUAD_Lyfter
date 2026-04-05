import csv
import os


def export_students_to_csv(students, path="students.csv"):
    """
    Export the list of student records to a CSV file.

    Parameters:
        students (list): List of student dictionaries.
        path (str): File path where the CSV will be saved.
    """

    # Check if there is data to export
    if not students:
        print("\nNo students to export.\n")
        return

    try:
        # Define CSV column headers based on student structure
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        # Open file in write mode (overwrites existing file)
        with open(path, mode="w", newline="", encoding="utf-8") as file:

            # Create a DictWriter to map dictionaries to CSV rows
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header row (column names)
            writer.writeheader()

            # Write all student records into the file
            writer.writerows(students)

        # Confirmation message
        print("-" * 42)
        print(f"\nData successfully exported to {path}\n")
        print("-" * 42)

    except Exception as e:
        # Handle unexpected errors during export
        print(f"Error exporting data: {e}")


def import_students_from_csv(path="students.csv"):
    """
    Import student records from a CSV file.

    Parameters:
        path (str): File path to read the CSV from.

    Returns:
        list: A list of student dictionaries.
    """

    # Check if the file exists before attempting to read it
    if not os.path.exists(path):
        print(f"\nFile '{path}' not found.\n")
        return []

    # Initialize an empty list to store imported students
    students = []

    try:
        # Open the CSV file in read mode
        with open(path, mode="r", encoding="utf-8") as file:

            # Create a DictReader to read rows as dictionaries
            reader = csv.DictReader(file)

            # Iterate through each row in the CSV file
            for i, row in enumerate(reader, start=1):
                try:
                    # Convert row data into a properly typed student dictionary
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish_grade": int(row["spanish_grade"]),
                        "english_grade": int(row["english_grade"]),
                        "social_studies_grade": int(row["social_studies_grade"]),
                        "science_grade": int(row["science_grade"])
                    }

                    # Add the student to the list
                    students.append(student)

                except KeyError as e:
                    # Handle missing columns in the CSV file
                    print(f"Missing column {e} in row #{i}")

                except ValueError:
                    # Handle invalid data types (e.g., non-integer grades)
                    print(f"Invalid data format in row #{i}")

        # Confirmation message after successful import
        print("-" * 44)
        print(f"\nData successfully imported from {path}\n")
        print("-" * 44)

        return students

    except Exception as e:
        # Handle unexpected errors during file reading
        print(f"Error importing data: {e}")
        return []