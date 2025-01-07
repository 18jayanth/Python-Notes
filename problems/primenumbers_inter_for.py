num=int(input("Enter a Number:"))
cnt=0
if num<=1:
    print("Not a Prime Number or a composite Number")
else:
    for i in range(2,num//2+1):
        if num%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")