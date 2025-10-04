#Create a class with following 
# a.data members: 1.Studentid  2.Name  3.Age   4.Percentage
# b.Add the following method: 1.Parameterized Constructor    2.Display    3.Accept    4.Method CalculateRank
#                             5.Override __str__ method

class Student:
    Students = []
    def __init__(self,sid=0,sname=" ",age=0,per=0):
        self.sid = sid
        self.sname = sname
        self.age = age
        self.per = per
        Student.Students.append(self)

    def accept(self):
        id = int(input("Enter student Id: "))
        name = input("Student Name: ")
        age = int(input("Enter Age: "))
        per = int(input("Enter Percentage: "))
        Student(id,name,age,per)
        
    
    def display(self):
        for s in Student.Students:
            print(s)


    def __str__(self):
        return f"\n Student Id:{self.sid}  \n Student Name: {self.sname} \n Student Age: {self.age} \n Student Percentage: {self.per}"
    

    def cal_Rank(self):
        ranked = sorted(Student.Students, key=lambda x: x.per, reverse=True)
        rank = 1
        for s in ranked:
            print(f"Rank {rank}: {s.sname} ({s.per}%)")
            rank += 1
        


if __name__ == "__main__":
   s1 =Student(1,"Raj",19,98)
   s2 =Student(2,"Riya",19,78)
   s3 =Student(4,"Vijay",20,88)
   s4 =Student(3,"Ajay",21,56)

   s1.display()
   s1.cal_Rank()

   