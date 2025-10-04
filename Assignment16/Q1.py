#Create a class Book with members as bid , bname , price and author . Add following method:
# a.Constructor  b.Destructor c.showbook d.Add static variable count and also maintain count of object created

class Book:
    count = 0
    def __init__(self,bid=0,bname=" ",price=0,author=" "):
        self.bid =bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def showbook(self):
        print(f"\nBook id: {self.bid} \n Book name: {self.bname} \n Book Price: {self.price} \n Book Author: {self.author}")
        print("Total books created (count):", Book.count)
        
        
    def __del__(self):
        print("Deconstruct the Object initialization")
        Book.count -+ 1


book1 = Book(101,"Yyati",420,"V.S.Khandekar")
book1.showbook()

book2 = Book(102, "Wings of Fire", 350, "A.P.J. Abdul Kalam")
book2.showbook()

print("\nCurrent Count:", Book.count)

    
