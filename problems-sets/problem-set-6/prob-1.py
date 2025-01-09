#1. Write a program to find the greatest of four numbers entered by the user

a=int(input("Enter 1st NUmber"))
b=int(input("Enter 2nd NUmber"))
c=int(input("Enter 3rd NUmber"))
d=int(input("Enter 4th NUmber"))
if(a>b and a>c and a>d):
    print("a is greater")
elif(b>a and b>c and b>d):
    print("b is greatest")
elif(c>a and c>b and c>d):
    print("c is greatest")
else:
    print("d is greatest")