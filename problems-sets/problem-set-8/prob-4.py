#4. Write a recursive function to calculate the sum of first n natural numbers.
n=int(input("Enter a Number:"))

def natural(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print("sum of first n natural numbers is",natural(n))
