#4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"square of two numbers is {self.n*self.n}")
    def cube(self):
        print(f"Cube of two numbers are:{self.n*self.n*self.n}")
    def squareroot(self):
        print(f"squareroot of two numbers are:{self.n**1/2}")
    @staticmethod
    def greet():
        print("hello")
        
n=Calculator(4)
n.square()
n.cube()
n.squareroot()
n.greet()