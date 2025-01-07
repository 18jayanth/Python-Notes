num=int(input("Enter a Number:"))
sum1=0
dup=num
while num!=0:
    rem=num%10
    sum1+=rem
    num//=10
if dup%sum1==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")