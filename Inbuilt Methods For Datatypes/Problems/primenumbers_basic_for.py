num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    for fact in range(1,num+1):
        if num%fact==0:
            cnt+=1
    if cnt==2:
        print("Prime Number")
    else:
        print("Not Prime Number")
