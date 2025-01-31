def factors(num,val=1,l=[]):
    if val>num:
        return l
    if num%val==0:
        l.append(val)
    return factors(num,val+1,l)
num=int(input("Enter a Number:"))
print(factors(num))