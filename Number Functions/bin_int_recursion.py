def bin_to_int(num,res=0,pos=0):
    if num==0:
        return res
    return bin_to_int(num//10,res+(num%10)*(2**pos),pos+1)
num1=int(input("Enter a Number:"))
print(bin_to_int(num1))