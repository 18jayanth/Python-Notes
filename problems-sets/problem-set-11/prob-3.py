class employee:
    salary=200
    increment=20
    def salaryincrement(self):
        return(self.salary +self.salary*(self.increment/100))
    @salaryincrement.setter
    def salaryincrement(self,salary):
         self.increment=((salary/self.salary)-1)*100
e=employee()
e.salaryincrement=280
print(e.salaryincrement)

