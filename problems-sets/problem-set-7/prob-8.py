""" 8. Write a program to print the following star pattern:
*
**
*** for n = 3 """
n=int(input("Enter a NUmber:"))
for i in range(1,n+1):
    print("*"*i,end="")
    print(" "*(n-i))