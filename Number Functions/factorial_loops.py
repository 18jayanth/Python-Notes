def fact(num,res=1):
    for i in range(1,num+1):
        res*=i
    return res
    pass
num=int(input("Enter a Number:"))
print(fact(num))