#Create a complex Number with data member as real and imag  and add following methods
#a.Constructor  b.Destructor   c.overload +,- operator

class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}i"
    
    def __add__(self,c2):
        c3 = Complex()
        c3.real = self.real + c2.real
        c3.imag = self.imag + c2.imag
        return c3
    
    def __sub__(self,c2):
        c4 = Complex()
        c4.real = self.real - c2.real
        c4.imag = self.imag - c2.imag
        return c4
    
    def __del__(self):
        print("Deconstructor")
    
obj1 = Complex(3,4)
print(obj1)

obj2 = Complex(1,2)
print(obj2)

obj3 = obj1 + obj2
#ob1.__add__(obj2)
print("Addition: ",obj3)

obj3 = obj1 - obj2
print("Sustraction: ",obj3)



