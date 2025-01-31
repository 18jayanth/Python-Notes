def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1
num=int(input("Enter a number:"))
if num<=1:
    print("not prime")
else:
    if prime(num):
        print("prime")
    else:
        print("not prime")