def disarum(num,power,res=0):
    if num==0:
        return res
    return disarum(num//10,power-1,res+(num%10)**power)
    pass
num=int(input('Enter a number:'))
power=len(str(num))
res=disarum(num,power)
if res==num:
    print("disarum number")
else:
    print("not disarum number")