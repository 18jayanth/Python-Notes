"""5. Write a class vector representing a vector of n dimensions. Overload the + and *
operator which calculates the sum and the dot(.) product of them"""
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,d2):
        result=Vector(self.i+d2.i,self.j+d2.j,self.k+d2.k)
        return result
    def __mul__(self,d2):
        
        
        result=(self.i*d2.i+self.j*d2.j+self.k*d2.k)
        return result
    def __str__(self):
        return f"Vector ({self.i}+{self.j}+{self.k})"
d1=Vector(1,2,3)
d2=Vector(2,3,4)
print(d1+d2)
print(d1*d2)
    
    
