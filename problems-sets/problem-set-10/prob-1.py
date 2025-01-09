"""1. Create a class “Programmer” for storing information of few programmers
working at Microsoft"""
class programmer():
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
    def getinfo(self):
        print(f"Employe name is {self.name} salary is{self.salary} and position is {self.position}")
harry=programmer("Jayanth","12000","Intern")
ajay=programmer("Ajay","15000","Engineer")
pavan=programmer("Pavan","20000","Analayst")
harry.getinfo()
ajay.getinfo()
pavan.getinfo()



