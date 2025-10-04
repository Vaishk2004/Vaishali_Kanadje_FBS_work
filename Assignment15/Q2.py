#Create a class Product with members as pid,pname,price and quality.Add following method
#a.Constructor  b.Destructor  c.ShowProduct

class Product:
    def __init__(self,pid,pname,price,quality):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quality = quality

    def showProduct(self):
        print("\nProduct Id: ",self.pid)
        print("Product Name: ",self.pname)
        print("Product Price: ",self.price)
        print("Product Quality: ",self.quality)

    def __del__(self):
        print("Deconstruct is Execute")



pid = int(input("Enter Product id: "))
pname = input("Enter Product Name: ")
price = int(input("Enter Price: "))
quality = input("Enter Quality: ")

obj1 = Product(pid,pname,price,quality)
obj1.showProduct()

obj2 = Product(11,'Laptop',41000,'Good')
obj2.showProduct()