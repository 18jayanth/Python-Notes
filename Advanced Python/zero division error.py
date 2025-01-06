"""try:
    a=int(input("enter 1st number:"))
    b=int(input("enter 2nd number:"))
    print(a/b)
except ZeroDivisionError as d:
    print(d)"""
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
if(b==0):
    raise ZeroDivisionError("hey it is diving by 0")
else:
    print(a/b)
#raise will crash the program sometimes its necessary so that programmer would know its mistakes
