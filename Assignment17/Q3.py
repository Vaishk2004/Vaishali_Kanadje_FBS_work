#Create a class MedicalStudent inherited from Student
# Add data members: Specialization     2.MarkofInternship
#Add Methods:  1.parameterized constructor  2.Display   3.  Accept    4.Override Method CalRank  5.override __str__ method

from Q1 import Student

from Q1 import Student

class MedicalStudent(Student):
    Students = []  
    def __init__(self, sid, sname, age, per, specialization="", markOfInternship=0):
        super().__init__(sid, sname, age, per)
        self.specialization = specialization
        self.markOfInternship = markOfInternship
        MedicalStudent.Students.append(self)

    def accept(self):
        sid = int(input("Enter Student Id: "))
        sname = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        per = float(input("Enter Percentage: "))
        specialization = input("Enter Specialization: ")
        markOfInternship = float(input("Enter Internship Marks: "))
        MedicalStudent(sid, sname, age, per, specialization, markOfInternship)

    def display(self):
        for s in MedicalStudent.Students:
            print(s)


    def __str__(self):
        return (f"\nStudent Id: {self.sid}"
                f"\nStudent Name: {self.sname}"
                f"\nStudent Age: {self.age}"
                f"\nStudent Percentage: {self.per}"
                f"\nSpecialization: {self.specialization}"
                f"\nInternship Marks: {self.markOfInternship}")


    def cal_Rank(self):
        ranked = sorted(MedicalStudent.Students,
                        key=lambda x: (x.per + x.markOfInternship),
                        reverse=True)
        rank = 1
        for s in ranked:
            print(f"Rank {rank}: {s.sname} (Total={s.per + s.markOfInternship})")
            rank += 1


if __name__ == "__main__":
    m1 = MedicalStudent(1, "Anita", 22, 82, "Cardiology", 12)
    m2 = MedicalStudent(2, "Rahul", 23, 76, "Neurology", 20)
    m3 = MedicalStudent(3, "Sneha", 21, 88, "Dermatology", 15)

    
    m1.display()

    m1.cal_Rank()
