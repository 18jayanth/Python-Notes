def int_to_bin(num,res=0,pos=1):
    if num==0:
        return res
    return int_to_bin(num//2,res+(num%2)*pos,pos*10)
num1=int(input("Enter a Number:"))
print(int_to_bin(num1))