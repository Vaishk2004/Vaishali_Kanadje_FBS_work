#Create a class Distance  with data member as km,m and cm  and add following methods
#a.Constructor  b.Destructor   c.overload +,- operator

class Distance:
    def __init__(self,km,m,cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __str__(self):
        return f"{self.km}km  {self.m}m  {self.cm}cm"
    
    def __add__(self,obj2):
        obj = Distance(0,0,0)
        obj.km = self.km + obj2.km
        obj.m = self.m + obj2.m
        obj.cm = self.cm + obj2.cm
        if obj.cm >= 100:
            obj.m += obj.cm // 100
            obj.cm = obj.cm % 100
        if obj.m >=1000:
            obj.km += obj.m // 1000
            obj.m = obj.m % 1000

        return obj

    def __sub__(self,obj2):
        obj = Distance(0,0,0)
        obj.km = self.km - obj2.km
        obj.m = self.m - obj2.m
        obj.cm = self.cm - obj2.cm
        if obj.cm >= 100:
            obj.m = obj.cm // 100
            obj.cm = obj.cm % 100
        if obj.m >=1000:
            obj.km = obj.m // 1000
            obj.m = obj.m % 1000

        return obj
    
    def __del__(self):
        print("Deconstructor")


obj1 = Distance(12,42,200)
print(obj1)

obj2 = Distance(11,40,100)
print(obj2)

obj3 = obj1 + obj2
print("Addition: ",obj3)

obj3 = obj1 - obj2
print('Substraction: ',obj3)

