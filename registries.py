

def add_study(record, id, name, last_name, program, state):
    #Add a student to the record
    estudiante = {"id": id,  "name": name, "last_name": last_name, "program": program, "state": state}
    record.append(estudiante)


def show_record(record):
    #Shows all students
    if not record:
        print("Empty record")
        return

    for i in record:
        print(f"Id: {i['id']} | Name: {i['name']} | Last_name: {i['last_name']} Program: {i['program']} | state: {i['state']}")


def search_student(record, id):
    #Search for a student by id
    for i in record:
        if i["id"] == id:
            return i
    return None


def update_information(record, id, new_program=None, new_state=None):
    #Update information
    update = search_student(record, id)
    if update:
        if new_program is not None:
            update["program"] = new_program
        if new_state is not None:
            update["state"] = new_state
        return True
    return False


def delete_student(record, name):
    #Delete a student
    p = search_student(record, name)
    if p:
        record.remove(p)
        return True
    return False

    