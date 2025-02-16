#prime and palindrome
def reverse(num):
    res=0
    while num!=0:
        rem=num%10
        res=res*10+rem
        num//=10
    return res
def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1
num=151
print('Palyprime' if prime(num) and  reverse(num)==num else 'not Palyprime')

