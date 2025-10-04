from SYMarks import SYMarks
from TYMarks import TYMarks

class Student:
    def __init__(self, roll_number, name, sy_marks, ty_marks):
        self.roll_number = roll_number
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self, total_marks):
        if total_marks >= 70:
            return "A"
        elif total_marks >= 60:
            return "B"
        elif total_marks >= 50:
            return "C"
        elif total_marks >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        total_computer_marks = self.sy_marks.computer_total + self.ty_marks.theory + self.ty_marks.practical
        grade = self.calculate_grade(total_computer_marks)

        
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        self.sy_marks.display()
        self.ty_marks.display()
        print(f"Total Computer Marks: {total_computer_marks}")
        print(f"Grade: {grade}")


if __name__ == "__main__":
    
    sy = SYMarks(computer_total=65, maths_total=70, electronics_total=60)

    
    ty = TYMarks(theory=20, practical=15)

    
    student = Student(roll_number=101, name="John Doe", sy_marks=sy, ty_marks=ty)

    
    student.display_result()
