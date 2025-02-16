def fascinating(num,val=1):
    if val>=10:
        return 1
    if str(val) not in a:
        return 0
    return fascinating(num,val+1)

num=191
a=str(num*1)+str(num*2)+str(num*3)
if fascinating(a):
    print("Fascinating Number")
else:
    print("Not Fascinating Number")