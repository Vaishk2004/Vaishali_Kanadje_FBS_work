#Create a class for shirt with members as sid,sname,type(formal etc.),price and size(small,large) . Add following methods:
# 1.constructor  2.Destructor   3.showshirt
# 4. for each size of shirt price should change by 10%
#     (eg.if 1000 is price then small price = 1000,medium = 1100,large=1200and xlarge=1300)
# Use static concept

class Shirt:
    price = 0
    def __init__(self,sid=0,sname=" ",type="formal",price=0,size=" "):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    

    def cal_Price(x):
        if x.size=="small":
            Shirt.price = x.price
        elif x.size=="medium":
            Shirt.price = x.price +(x.price * 0.10)
        elif x.size=="large":
            Shirt.price = x.price +(x.price * 0.20)
        elif x.size=="xlarge":
            Shirt.price = x.price +(x.price * 0.30)
        return Shirt.price
        
    
    def showshirt(self):
        print("\nShirt Id: ",self.sid)
        print("Shirt name: ",self.sname)
        print("Shirt type: ",self.type)
        print("Shirt price: ",Shirt.price)
        print("Shirt size: ",self.size)
    
    
    def __del__(self):
        print("Destructor is call")


shirt1 = Shirt(11,"Urban","Formal",1000,"medium")
Shirt.cal_Price(shirt1)
shirt1.showshirt()

shirt2 = Shirt(12,"Classic","Casual",1000,"xlarge")
Shirt.cal_Price(shirt2)
shirt2.showshirt()