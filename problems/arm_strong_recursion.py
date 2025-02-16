def arm_strong(num,length,res=0):
    
    if num==0:
        return res
    return arm_strong(num//10,length,res+(num%10)**length)
num=int(input("Enter a Number:"))
length=len(str(num))
res=arm_strong(num,length)
if num==res:
    print("Arm Strong Number:")
else:
    print("not arm strong number:")