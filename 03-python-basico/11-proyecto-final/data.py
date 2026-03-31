import actions
import csv
import os


def export_students_to_csv(path="students.csv"):
    """
    Export the list of student records to a CSV file.
    """

    # Validate that there is data available to export
    if not actions.students:
        print("\nNo students to export.\n")
        return  # Exit early if there is no data

    try:
        # Define the CSV column headers based on student dictionary keys
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        # Open the file in write mode (this will overwrite existing content)
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            # Create a DictWriter object to map dictionaries to CSV rows
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header row (column names)
            writer.writeheader()

            # Write all student records as rows in the CSV file
            writer.writerows(actions.students)

        # Confirmation message after successful export
        print(f"\nData successfully exported to {path}\n")

    except Exception as e:
        # Handle any unexpected error during file writing
        print(f"Error exporting data: {e}")


def import_students_from_csv(path="students.csv"):
    """
    Import student records from a CSV file and store them in the global list.
    """

    # Check if the file exists
    if not os.path.exists(path):
        print(f"\nFile '{path}' not found. Please export data first with option 5 in the menu.\n")
        return  # Exit if file does not exist

    try:
        # Open the file in read mode
        with open(path, mode="r", encoding="utf-8") as file:
            # Create a DictReader to read each row as a dictionary
            reader = csv.DictReader(file)

            # Clear existing data to avoid duplication
            actions.students.clear()

            # Iterate through each row in the CSV file
            for i, row in enumerate(reader, start=1):
                try:
                    # Convert string values to appropriate data types (int for grades)
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish_grade": int(row["spanish_grade"]),
                        "english_grade": int(row["english_grade"]),
                        "social_studies_grade": int(row["social_studies_grade"]),
                        "science_grade": int(row["science_grade"])
                    }

                    # Append the validated student record to the global list
                    actions.students.append(student)

                except KeyError as e:
                    # Handle missing columns in the CSV file
                    print(f"Missing column {e} in row #{i}")
                except ValueError:
                    # Handle invalid data types
                    print(f"Invalid data format in row #{i}")

        # Confirmation message after successful import
        print(f"\nData successfully imported from {path}\n")

    except Exception as e:
        # Handle any unexpected error during file reading
        print(f"Error importing data: {e}")