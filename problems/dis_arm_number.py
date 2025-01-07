num = int(input("Enter a Number:"))
sum1=0
dup=num
power=len(str(num))

sum1+=0
while num!=0:
    rem=num%10
    sum1+=rem**power
    num=num//10
    power-=1
print(sum1)
if sum1==dup:
    print("Dis arum Number")
else:
    print("Not a Dis arum  NUmber")