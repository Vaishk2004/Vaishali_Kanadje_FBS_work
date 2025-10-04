# Create a class Book with members as bid, bname , price and author . add following method
#a.constructor  b.destructor  c.showbook

class Book:
    def __init__(self,bid=0,bname="",price=0,author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showbook(self):
        print("\nBook id: ",self.bid)
        print("Book name: ",self.bname)
        print("Book Price: ",self.price)
        print("Book Author: ",self.author)

    def __del__(self):
        print("Deconstruct is Execute")


bid = int(input("Enter Book id: "))
bname = input("Enter Book name: ")
price = int(input("Enter price: "))
author = input("Enter Author name: ")


obj1 = Book(bid,bname,price,author)
obj1.showbook()


obj2 = Book(121,'Yayati',699,'V.S.Khandekar')
obj2.showbook()