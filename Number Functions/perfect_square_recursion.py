def perfect(num,val=1):
    if val>num:
        return 0
    if val*val==num:
        return 1
    return perfect(num,val+1)
    pass
num=int(input("Enter a Number:"))
if perfect(num):
    print("perfect square")
else:
    print("not perfect square")