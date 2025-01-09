#1. Write a program using functions to find greatest of three numbers.
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
def great():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print(f"Greatest of Three Numbers is:{great()}")
