#not palindrome
#prime reverse also prime
def reverse(num,res=0):
    if num==0:
        return res
    return reverse(num//10,res*10+num%10)
def prime(num,val=1):
    if val==num+1:
        return 1
    if num%val==0:
        return 1+prime(num,val+1)
    return prime(num,val+1)
num=17
a=reverse(num)
print('EMIRP' if a!=num and prime(num) and prime(a) else 'not EMIRP')