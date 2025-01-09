#2. Write a class “Calculator” capable of finding square, cube and square root of a
#number.
class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"square of two numbers is {self.n*self.n}")
    def cube(self):
        print(f"Cube of two numbers are:{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"squareroot of two numbers are:{self.n**1/2}")
n=Calculator(4)
n.square()
n.cube()
n.squareroot()