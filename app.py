from registries import *

# Main 
record = []

while True:
    print("\n=== MENU ===")
    print("1. Register")
    print("2. Consult list")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    option = input("Select: ")

    if option == "1":
        # Student data
        try:
            student_id = int(input("Id: "))
            name = input("Name: ")
            last_name = input("Last name: ")
            program = input("Program: ")
            state = input("State: ")
            add_student(record, student_id, name, last_name, program, state)
            print("Student registered successfully.")
        except ValueError:
            print("Error: ID must be a number.")

    elif option == "2":
        show_records(record)

    elif option == "3":
        # Search by ID 
        try:
            search_id = int(input("Enter ID to search: "))
            p = search_student(record, search_id)
            print(p if p else "Student not found")
        except ValueError:
            print("Error: Please enter a valid numerical ID.")

    elif option == "4":
        # Update information 
        try:
            student_id = int(input("ID of student to update: "))
            new_program = input("New program (press enter to skip): ")
            new_state = input("New state (press enter to skip): ")
            
            result = update_information(record, student_id, new_program, new_state)
            if result:
                print("Information updated successfully.")
            else:
                print("Student not found.")
        except ValueError:
            print("Error: ID must be a number.")

    elif option == "5":
        # Delete by ID 
        try:
            delete_id = int(input("Enter ID to delete: "))
            if delete_student(record, delete_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        except ValueError:
            print("Error: ID must be a number.")
    
    elif option == "6":
        print("Exiting")
        break

    else:
        print("Invalid option")