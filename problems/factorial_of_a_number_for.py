num=int(input("Enter a Number:"))
prod=1
for factor in range(1,num+1):
    prod*=factor
print(prod)