"""4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
handling the ‘ZeroDivisionError’."""
try:
    a=int(input("Enter a NUmber"))
    b=int(input("Enter a NUmber"))
    d=a/b
    print(d)
except ZeroDivisionError as z:
    print("it should not be divisible by 0")