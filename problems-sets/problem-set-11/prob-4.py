"""4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them"""
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,d2):
        return Complex(self.r+d2.r,self.i+d2.i)
    def __mul__(self,d2):
        
        real_part = self.r * d2.r - self.i * d2.i
        imaginary_part = self.r * d2.i + self.i * d2.r
        return Complex(real_part, imaginary_part)
    def __str__(self):
        return f"{self.r}+{self.i}i"
d1=Complex(1,2)
d2=Complex(2,3)
print(d1+d2)
    
    
        

    


