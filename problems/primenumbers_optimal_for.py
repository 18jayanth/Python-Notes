import math
num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    for fact in range(2,num**2+1):
        if num%fact==0:
            print("Not a Prime Number")
            break

    else:
        print("Not Prime Number")
