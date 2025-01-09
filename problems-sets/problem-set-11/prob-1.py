#1. Create a class (2-D vector) and use it to create another class representing a 3-D vector
class twod:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def set(self):
        print(f"values are {self.i}i+{self.j}j")

class threed(twod):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def set(self):
        print(f"values are {self.i}i+{self.j}j+{self.k}k")
har=twod(1,2)
har.set()
tar=threed(1,2,3)
tar.set()



    