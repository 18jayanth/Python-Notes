try:
    a=int(input("enter a Number"))
    print(a)
except ValueError as e:
    print("hii")
    print(e)
else :
    print("executed successfully")
#if try works then else or else except