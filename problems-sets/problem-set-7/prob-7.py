"""7. Write a program to print the following star pattern.
 *
***
***** for n = 3"""
# for 1 n-1 spaces 2*i-1 stars
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    
    
