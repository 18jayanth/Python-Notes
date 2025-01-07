import math
num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    fact=2
    while fact<=int(num**0.5):
        if num%fact==0:
            print("Not a Prime Number")
            break
        fact+=1

    else:
        print("Prime Number")
