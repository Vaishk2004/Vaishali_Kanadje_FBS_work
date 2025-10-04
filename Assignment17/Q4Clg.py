#Create  a class College which contain collection of students
#Add method : 1. parameterized constructor for number students     2.AddStudent   3. Getstudent   4.RemoveStudent.   5.Override __str__ method

from Q1 import Student
class College:
    def __init__(self):
        cname = "SBES"
        
        self.students = []

    def addStu(self):
        id = int(input("Enter student Id: "))
        name = input("Student Name: ")
        age = int(input("Enter Age: "))
        per = int(input("Enter Percentage: "))
        s = Student(id,name,age,per)
        self.students.append(s)

    def getStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                print(s) 
        print("Not Found")

    def removeStudent(self, sid):
        for s in self.students:
            if s.sid == sid:
                self.students.remove(s)
                print(f"Student {s.sname} removed successfully!")
                break
        print(" Student not found!")

    def __str__(self):
        details = f"\nCollege Name: {self.cname}\nStudents:\n"
        for s in self.students:
            details += str(s) + "\n"
        return details


if __name__ == "__main__":
    c = College()
    c.addStu()
    c.addStu()
    print(c)
    