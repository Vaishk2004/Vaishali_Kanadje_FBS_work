class Emp:
    def __init__(self,eid=0,ename="",basic=0):
        self.eid = eid
        self.ename = ename
        self.basic = basic
        

    def __str__(self):
        return f"{self.eid}, {self.ename}, {self.basic}"