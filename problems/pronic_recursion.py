def pronic(num,val=1):
    if val>num:
        return 0
    if val*(val+1)==num:
        return 1
    return pronic(num,val+1)
num1=int(input('Enter a Number:'))
if pronic(num1):
    print("pronic number:")
else:
    print("not pronic  number:")