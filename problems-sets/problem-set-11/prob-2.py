"""2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog’."""
class animals:
    @staticmethod
    def makesound():
        print("huss huss")
    pass

class pets(animals):
    @staticmethod
    def sound():
        print("meow")
    pass
    
class dog(pets):
    @staticmethod
    def bark():
        print("bow bow")
d=dog()
d.bark() # bow bow
d.sound() # meow
d.makesound() # huss huss

