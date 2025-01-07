num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    fact=1
    while(fact<=num):
        if num%fact==0:
            cnt+=1
        fact+=1
    if cnt==2:
        print("Prime Number")
    else:
        print("Not Prime Number")
