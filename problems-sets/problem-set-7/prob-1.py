#1. Write a program to print multiplication table of a given number using for loop.
Number=int(input("Enter Your Number::"))
for i in range(1,11):
    print(f"{Number} * {i}={Number*i}")