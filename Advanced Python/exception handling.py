
try:
    a=int(input("enter a Number"))
    print(a)
except ValueError as e:
    print("hii")
    print(e)
except Exception as e:
    print(e)
print("Thank You")
# it prints the error but the program has not been crashed

