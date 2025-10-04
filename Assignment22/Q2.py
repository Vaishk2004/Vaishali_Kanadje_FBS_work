from Q1 import Emp
import pickle

def add_record():
    emp = Emp()
    emp.eid = int(input("Enter Employee ID: "))
    emp.ename = input("Enter Employee Name: ")
    emp.basic = float(input("Enter Salary: "))

    with open("Assignment22/record.txt", 'ab') as fp:
        pickle.dump(emp, fp)
    print("Record added successfully!")


def search_record():
    eid = int(input("Enter Employee Id: "))
    found = False

    try:
        with open("Assignment22/record.txt", 'rb') as fp:
            try:
                while True:
                    emp = pickle.load(fp)
                    if emp.eid == eid:
                        print("Record Found:", emp)
                        found = True
                        break
            except EOFError:
                pass
    except FileNotFoundError:
        pass

    if not found:
        print("Not found")


def delete_record():
    eid = int(input("Enter Employee Id: "))
    found = False
    container = []

    try:
        with open("Assignment22/record.txt", 'rb') as fp:
            try:
                while True:
                    emp = pickle.load(fp)
                    if emp.eid == eid:
                        found = True
                    else:
                        container.append(emp)
            except EOFError:
                pass
    except FileNotFoundError:
        pass

    if found:
        with open("Assignment22/record.txt", 'wb') as fp:
            for emp in container:
                pickle.dump(emp, fp)
        print('Record deleted Successfully!!!')
    else:
        print("Record not found.")


def edit_record():
    eid = int(input("Enter Employee Id: "))
    found = False
    container = []

    try:
        with open("Assignment22/record.txt", 'rb') as fp:
            try:
                while True:
                    emp = pickle.load(fp)
                    if emp.eid == eid:
                        found = True
                        print("1. Name")
                        print("2. Salary")
                        ch = int(input("Enter Choice for Edit: "))
                        if ch == 1:
                            emp.ename = input("Enter new name: ")
                        elif ch == 2:
                            emp.basic = float(input('Enter new Salary: '))
                        else:
                            print('Enter correct choice')
                    container.append(emp)
            except EOFError:
                pass
    except FileNotFoundError:
        pass

    if not found:
        print("Not found")
    else:
        with open("Assignment22/record.txt", 'wb') as fp:
            for emp in container:
                pickle.dump(emp, fp)
        print('Record Edited Successfully!!!')


def display_record():
    try:
        with open("Assignment22/record.txt", 'rb') as fp:
            try:
                while True:
                    emp = pickle.load(fp)
                    print(emp)
            except EOFError:
                pass
    except FileNotFoundError:
        print("No records found.")


if __name__ == "__main__":
    ch = 0
    while ch != 6:
        print("\n1. Add a record")
        print("2. Search for a record using id")
        print("3. Delete record using id")
        print("4. Edit a record using id")
        print("5. Display all records")
        print("6. Exit")

        ch = int(input("Enter choice: "))
        if ch == 1:
            add_record()
        elif ch == 2:
            search_record()
        elif ch == 3:
            delete_record()
        elif ch == 4:
            edit_record()
        elif ch == 5:
            display_record()
        elif ch == 6:
            print('Exit')
            break
        else:
            print("Enter correct choice")
