def perfect(num,val=1,res=0):
    if val>num//2:
        return res
    if num%val==0:
        res+=val
    return perfect(num,val+1,res)
num=int(input("Enter a number:"))
res=perfect(num)
if num == res:
    print("perfect")
else:
    print("not perfect")
