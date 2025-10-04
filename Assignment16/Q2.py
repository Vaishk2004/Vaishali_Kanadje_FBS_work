# Create a class product with members as pid,pname,price and quality . Add following method:
# a. constructor     b.destructor     c.showproduct 
# d.add static member discount     e.Provide method for applying discount on price of product

class Product:
    discount = 0.10
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

    def discount_product(self):
        print("Total Discount: ",self.price * Product.discount)

    def __del__(self):
        print("Deconstruct is Execute")


pro1 = Product(101,"Laptop",41000,"Good")
pro1.showProduct()

pro1.discount_product()
