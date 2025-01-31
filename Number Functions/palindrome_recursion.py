def palindrome(num,res=0):
    if num==0:
        return res
    return palindrome(num//10,res*10+(num%10))
    pass
num1=int(input("Enter a Number"))
res1=palindrome(num1)
if res1==num1:
    print("Palindrome")
else:
    print("Not palindrome")
