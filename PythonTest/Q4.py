class Book:
    def __init__(self,bno=0,bname="",author="",cost=0):
        self.bno = bno
        self.bname = bname
        self.author = author
        self.cost = cost

    def __str__(self):
        return f"{self.bno},{self.bname},{self.author},{self.cost}"
    
    def addbook(self):
        bno = int(input("Enter Book Number: "))
        bname = input("Enter Book Name: ")
        bauthor = input("Enter Book Author: ")
        bcost = int(input("Enter Book Cost: "))
        b = Book(bno,bname,bauthor,bcost)
        with open("PythonTest/data.txt","a") as f1:
                    f1.write(str(b))


    def update(self):
        a = int(input("Enter book no: "))
        container = []
        found = False
        with open("PythonTest/data.txt","r") as f1:
            for b in f1:
                list1= b.strip().split(",")
                if list1[0] == str(a):
                    found = True
                    price = int(input("Enter new Price: "))
                    list1[3] = str(price)
                container.append(b)
        
        if found == True:
            with open("PythonTest/data.txt","w") as f1:
                for b in container:
                    f1.write(b)
        else:
            print("Not Found")
    
    def delete(self):
        a = int(input("Enter book no: "))
        container = []
        found = False
        with open("PythonTest/data.txt","r") as f1:
            for b in f1:
                list1= b.strip().split(",")
                if list1[0] == str(a):
                    found = True
                else:
                    container.append(b)
        
        if found == True:
            with open("PythonTest/data.txt","w") as f1:
                for b in container:
                    f1.write(b)
                    print("Deleted Successfully!!")
        else:
             print("Not Found")
                

    def showAll(self):
        with open("PythonTest/data.txt","r") as f1:
            for b in f1:
                bno,bname,author,cost = b.strip().split(",")
                print(f"Book No:{bno},Book name:{bname},Book Author:{author},Cost:{cost}")
    

obj = Book()
while True:
    print("1.Add Book")
    print("2.Update")
    print("3.Delete")
    print("4.Show All Data")
    print("5.Show Specific Data")
    ch = int(input("Enter Choice: "))
    if ch==1:
        obj.addbook()
    elif ch==2:
        obj.update()
    elif ch == 3:
        obj.delete() 
    elif ch == 4:
        obj.showAll()

             