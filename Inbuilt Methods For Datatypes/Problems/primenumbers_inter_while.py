num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    fact=2
    while fact<=num//2:
        if num%fact==0:
            print(" Not Prime Number")
            break
        fact+=1
    else:
        print(" prime Number")
