#prime and palindrome
def reverse(num,res=0):
    if num==0:
        return res
    return reverse(num//10,res*10+num%10)
def prime(num,val=1):
    if val==num+1:
        return 0
    if num%val==0:
        return 1+prime(num,val+1)
    else:
        return prime(num,val+1)

num=151
print('Palyprime' if   prime(num)==2 and reverse(num)==num else 'not Palyprime')

