def single(num,res=0):
    if num==0:
        return res
    return single(num//10,res+(num%10)**2)
def happy(num):
    if num<10 and (num==1 or num==7):
        return 1
    elif num<10:
        return 0
    else:
        num=single(num)
    return happy(num)
num1=20
if happy(num1):
    print("happy Number")
else:
    print("not happy number")
