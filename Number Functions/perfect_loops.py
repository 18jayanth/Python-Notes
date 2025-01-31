def perfect(num,res=0):
    for i in range(1,num//2+1):
        if num%i==0:
            res+=i
    if num==res:
        return ("perfect")
    else:
        return ("not perfect")
num=int(input("Enter a number:"))
print(perfect(num))
#dont forget to return function dont print inside
