students = [  # Global list to store all student records
    {
        "name": "Juan Perez",
        "section": "10A",
        "spanish_grade": 85,
        "english_grade": 90,
        "social_studies_grade": 88,
        "science_grade": 92
    },
    {
        "name": "Maria Gonzalez",
        "section": "11B",
        "spanish_grade": 95,
        "english_grade": 93,
        "social_studies_grade": 91,
        "science_grade": 94
    },
    {
        "name": "Carlos Ramirez",
        "section": "11A",
        "spanish_grade": 78,
        "english_grade": 82,
        "social_studies_grade": 80,
        "science_grade": 76
    },
    {
        "name": "Ana Lopez",
        "section": "9C",
        "spanish_grade": 88,
        "english_grade": 87,
        "social_studies_grade": 90,
        "science_grade": 89
    }
] 


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


def get_average(student):
    """
    Calculate and return the average grade of a student.
    """
    try:
        return (
            student["spanish_grade"] +
            student["english_grade"] +
            student["social_studies_grade"] +
            student["science_grade"]
        ) / 4
    except KeyError as e:
        # Handle missing grade fields in the dictionary
        print(f"Missing key in student data: {e}")
        return 0
    except Exception as e:
        # Handle any unexpected error
        print(f"Unexpected error while calculating average: {e}")
        return 0


def get_top3_average_grades():
    """
    Retrieve and display the top 3 students with the highest average grades.
    """

    # Check if there are students registered
    if not students:
        print("\nNo students registered.\n")
        return 

    try:
        # Sort students using a helper function
        sorted_students = sorted(
            students,
            key=get_average,   # Function used to calculate sorting value
            reverse=True      # Sort from highest to lowest
        )

        # Get the top 3 students (safe even if there are less than 3)
        top3 = sorted_students[:3]

        print("\n=== Top 3 Students ===\n")

        # Display results
        for i, student in enumerate(top3, start=1):
            try:
                avg = get_average(student)

                print(f"#{i} {student.get('name', 'N/A')}")
                print(f"Average: {avg:.2f}")
                print("-" * 30)

            except Exception as e:
                # Handle unexpected errors while displaying a student
                print(f"Error displaying student #{i}: {e}")

    except Exception as e:
        # Handle errors during sorting
        print(f"Error while processing top students: {e}")


def get_students_overall_average():
    """
    Retrieve and display the overall average grade across all students.
    This represents the average of each student's individual average grade.
    """

    # Validate that there are students registered
    if not students:
        print("\nNo students registered.\n")
        return  # Exit early if no data is available

    list_of_averages = []

    try:
        # Calculate the average for each student and store it in a list
        for i, student in enumerate(students, start=1):
            try:
                avg = get_average(student)  # Reuse existing function
                list_of_averages.append(avg)
            except Exception as e:
                # Handle unexpected errors per student without stopping the loop
                print(f"Error processing student #{i}: {e}")

        # Ensure we have valid averages before calculating the final result
        if not list_of_averages:
            print("\nNo valid student averages available.\n")
            return

        # Calculates overall average (average of averages)
        overall_average = sum(list_of_averages) / len(list_of_averages)

        # Display result in a formatted way
        print("-" * 53)
        print(f"\nThe overall average grade of all students is: {overall_average:.2f}\n")
        print("-" * 53)

    except ZeroDivisionError:
        # Handle division by zero (extra safety, though already validated)
        print("Error: Cannot calculate average due to division by zero.")
    except Exception as e:
        # Catch any unexpected error in the overall process
        print(f"Unexpected error while calculating overall average: {e}")