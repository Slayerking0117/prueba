
def add_student(record, student_id, name, last_name, program, state):
    """
    Creates a student dictionary and adds it to the list.
    """
    student = {
        "id": student_id, 
        "name": name, 
        "last_name": last_name, 
        "program": program, 
        "state": state
    }
    record.append(student)


def show_records(record):
    """
    Prints all students currently in the record.
    """
    if not record:
        print("Empty record")
        return

    for i in record:
        print(f"Id: {i['id']} | Name: {i['name']} | Last_name: {i['last_name']} | Program: {i['program']} | State: {i['state']}")


def search_student(record, student_id):
    """
    Searches for a student by ID. Returns the student dictionary or None.
    """
    for i in record:
        if i["id"] == student_id:
            return i
    return None


def update_information(record, student_id, new_program=None, new_state=None):
    """
    Updates the program and/or state of a student found by ID.
    """
    student = search_student(record, student_id)
    if student:
        if new_program:
            student["program"] = new_program
        if new_state:
            student["state"] = new_state
        return student
    return False


def delete_student(record, student_id):
    """
    Searches for a student by ID and removes them from the record.
    """
    student = search_student(record, student_id)
    if student:
        record.remove(student)
        return True
    return False