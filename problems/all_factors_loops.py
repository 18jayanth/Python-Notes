def factors(num,l=[]):
    l.append(1)
    for i in range(2,num//2+1):
        if num%i==0:
            l.append(i)
    l.append(num)
    return l

num=int(input("Enter a Number:"))
print(factors(num))