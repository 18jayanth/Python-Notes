#6. Write a python function which converts inches to cm
def conversion(inches):
    d=inches*2.54
    return d
inches=int(input("Enter height in inches:"))
conversion(inches)
print("height in cm is ",conversion(inches))