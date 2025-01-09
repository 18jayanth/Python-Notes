#5. Write a program to find the sum of first n natural numbers using while loop.
sum=0
i=1
n=int(input("Enter a Number:"))
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)