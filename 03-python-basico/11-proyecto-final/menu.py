import actions
import data

def display_menu(students):
    while True:
        print("""
   _____ _             _            _   
  / ____| |           | |          | |  
 | (___ | |_ _   _  __| | ___ _ __ | |_ 
  \___ \| __| | | |/ _` |/ _ \ '_ \| __|
  ____) | |_| |_| | (_| |  __/ | | | |_ 
 |_____/ \__|\__,_|\__,_|\___|_| |_|\__|
                                        
   __  __                                    _   
  |  \/  |                                  | |  
  | \  / | __ _ _ __   __ _  __ _  ___ _ __  | |_ 
  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ \ | __|
  | |  | | (_| | | | | (_| | (_| |  __/ | | || |_ 
  |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| \__|
                             __/ |               
                            |___/                

               S Y S T E M
""")
        print("1. Add new student")
        print("2. List all students")
        print("3. Top 3 - Highest averages")
        print("4. View overall average grade of all students")
        print("5. Failed students")
        print("6. Export data to CSV")
        print("7. Import data from a CSV (previously exported)")
        print("8. Delete Student")
        print("9. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            actions.insert_students(students)

        elif option == "2":
            actions.get_all_students(students)

        elif option == "3":
            actions.get_top3_average_grades(students)

        elif option == "4":
            actions.get_students_overall_average(students)

        elif option == "5":
            actions.get_failed_students(students)

        elif option == "6":
            data.export_students_to_csv(students)

        elif option == "7":
            students = data.import_students_from_csv()

        elif option == "8":
            actions.delete_student(students)

        elif option == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option")
