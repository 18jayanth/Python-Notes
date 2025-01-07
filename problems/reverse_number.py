num=int(input("Enter a Number:"))
length=len(str(num))-1
rev=0
while num!=0:
    rem=num%10
    rev=rev+rem*(10**length)
    num=num//10
    length=length-1
print(f"Reverse a Number:{rev}")