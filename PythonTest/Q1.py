class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h}h  {self.m}m  {self.s}s"
    
    def __add__(self,obj2):
        obj = Time(0,0,0)
        obj.h = self.h + obj2.h
        obj.m = self.m + obj2.m
        obj.s = self.s + obj2.s
        if obj.s >= 60:
            obj.m += obj.s//60
            obj.s = obj.s % 60
        if obj.m >= 60:
            obj.h += obj.m//60
            obj.m = obj.m % 60
        return obj

timezone1 = Time(12,2,120) 
timezone2 = Time(1,60,30) 

addition = timezone1 + timezone2
print(addition)