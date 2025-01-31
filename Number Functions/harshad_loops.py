def harshad(num,res=0):
    dup=num
    while num!=0:
        rem=num%10
        res+=rem
        num//=10
    if dup%res==0:
        return 1
    else:
        return 0
num1=int(input("Enter a Number:"))
if harshad(num1):
    print("Harshad Number")
else:
    print("not harshad number")