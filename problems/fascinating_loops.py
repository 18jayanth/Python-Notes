def fascinating(num):
    for val in range(1,10):
        if str(val) not in num:
            return 0
    return 1
    pass
num=219
a=str(num*1)+str(num*2)+str(num*3)
if fascinating(a):
    print("Fascinating Number")
else:
    print("Not Fascinating Number")