#4. Write a program to find whether a given number is prime or not
number=int(input("enter a Number:"))
count=0
for i in range(2,number):
    if(number%i==0):
        print("composite")
        break;
else:
    print("prime")
