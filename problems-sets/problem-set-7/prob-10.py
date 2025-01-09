""" 10. Write a program to print multiplication table of n using for loops in reversed
order.
  1 5*10=50
  2  5*9=45
  3  5*8=40
  ................"""
n=int(input("Enter a Number:"))
for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")