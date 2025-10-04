#Create a derived class for student
#Add Data member: 1.branch  2.internalMarks
#Add methods: 1.parametirezed constructor   2.Display    3. Accept    4.Override method calculateRank    5.Override __str__ method

from Q1 import Student

class EnggStudent(Student):
    Students = []
    def __init__(self,sid,sname,age,per,branch=" ",intMark=0):
        super().__init__(sid, sname, age, per)
        self.branch = branch
        self.intMark = intMark
        EnggStudent.Students.append(self)

    def accept(self):
        sid = int(input("Enter Student Id: "))
        sname = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        per = float(input("Enter Percentage: "))
        branch = input("Enter Branch: ")
        intMark = float(input("Enter Internal Marks: "))
        EnggStudent(sid, sname, age, per, branch, intMark)

    def display(self):
        for s in EnggStudent.Students:
            print(s)

    def __str__(self):
        return (f"\nStudent Id: {self.sid} \nStudent Name: {self.sname} \nStudent Age: {self.age} \nStudent Percentage: {self.per}"
                f"\nBranch: {self.branch} \nInternal Marks: {self.intMark}")
    
    def cal_Rank(self):
        ranked = sorted(EnggStudent.Students,key=lambda x: (x.per + x.intMark),reverse=True)
        rank = 1
        for s in ranked:
            print(f"Rank {rank}: {s.sname} (Total={s.per + s.intMark})")
            rank += 1


if __name__ == "__main__":
    e1 = EnggStudent(1, "Raj", 19, 80, "CSE", 15)
    e2 = EnggStudent(2, "Riya", 20, 85, "IT", 10)
    e3 = EnggStudent(3, "Ajay", 21, 70, "Mech", 20)

    e1.display()

    e1.cal_Rank()