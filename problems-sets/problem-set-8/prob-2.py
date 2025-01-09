#2. Write a python program using function to convert Celsius to Fahrenheit
temp1=int(input("Enter Temperature:"))
def temp(temp1):
    temp2=(temp1*9)/5+32
    return temp2
print('temperature in Fahrenheit is ',temp(temp1))
