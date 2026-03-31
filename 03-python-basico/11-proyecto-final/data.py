import actions
import csv

def export_students_to_csv(path="students.csv"):
    """
    Export the students list to a CSV file.
    """

    # Validate that there is data to export
    if not actions.students:
        print("\nNo students to export.\n")
        return

    try:
        # Define CSV column headers (keys from dictionary)
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

            # Write header row
            writer.writeheader()

            # Write each student as a row
            writer.writerows(actions.students)

        print(f"\nData successfully exported to {path}\n")

    except Exception as e:
        print(f"Error exporting data: {e}")