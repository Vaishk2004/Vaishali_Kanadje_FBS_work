# Create a class with Shirt with membwers as sid,sname,type(formal etc),price and size(small ,large etc). Add following method:
# a.constructor  b.destructor  c.showShirt

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def showShirt(self):
        print("\n Shirt Id: ",self.sid)
        print("Shirt Name: ",self.sname)
        print("Shirt Type: ",self.type)
        print("Shirt Price: ",self.price)
        print("Shirt Size: ",self.size)

    def __del__(self):
        print("Deconstruct is Execute")


    
id = int(input("Enter shirt Id: "))
name = input("Enter Shirt Name: ")
type = input("Enter type of shirt: ")
price = int(input("Enter price: "))
size = input("Enter size(Small/large): ")

obj1 = Shirt(id,name,type,price,size)
obj1.showShirt()

obj2 = Shirt(11,'Zara','Formal',1200,'Small')
obj2.showShirt()