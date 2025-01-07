num = int(input("Enter a Number:"))
sum1=0
for i in range(1, num//2+1):
    if num % i == 0:
        sum1+=i

if sum1==num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")