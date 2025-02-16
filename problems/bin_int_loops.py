def bin_to_int(num,res=0,pos=0):
    while num!=0:
        rem=num%10
        res+=rem*(2**pos)
        num//=10
        pos+=1
    return res
num1=int(input("Enter a Number:"))
print(bin_to_int(num1))