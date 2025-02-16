def palindrome(num,res=0):
    dup=num
    while num!=0:
        rem=num%10
        res=res*10+rem
        num//=10
    if dup==res:
        return 1
    else:
        return 0
    pass
num1=int(input("Enter a Number:"))
if palindrome(num1):
    print("Palindrome")
else:
    print("not palindrome")