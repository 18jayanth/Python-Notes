def int_to_bin(num,res=0,pos=1):

    while num!=0:
        rem=num%2
        res+=rem*pos
        num//=2
        pos*=10
    return res
num1=int(input("Enter a Number:"))
print(int_to_bin(num1))
