import actions
import data

def display_menu():
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
        print("5. Export data to CSV")
        print("6. Import data from a CSV (previously exported)")
        print("7. Delete Student)")
        print("8. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            actions.insert_student()

        elif option == "2":
            actions.get_all_students()

        elif option == "3":
            actions.get_top3_average_grades()

        elif option == "4":
            actions.get_students_overall_average()

        elif option == "5":
            data.export_students_to_csv()

        elif option == "6":
            data.import_students_from_csv()

        elif option == "7":
            actions.delete_student()

        elif option == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option")
