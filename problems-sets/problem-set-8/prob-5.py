""" 5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
* """
def pattern(n):
    for i in range(1,n+1):
        print("*"*(n+1-i),end="")
        print(" "*(i-1))
pattern(3)