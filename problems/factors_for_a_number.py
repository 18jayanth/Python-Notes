num=int(input("Enter a Number:"))
l=[]
for i in range(1,num+1):
    if num%i==0:
        l.append(i)

print(l)
