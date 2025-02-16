def pronic(num,val=1):
    while val<=num:
        if val*(val+1)==num:
            return 1
        val+=1
    return 0
    pass
num=int(input('Enter a Number:'))
if pronic(num):
    print("pronic number:")
else:
    print("not pronic  number:")
