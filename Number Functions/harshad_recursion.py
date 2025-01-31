def harshad(num,res=0):
    if num==0:
        return res
    return harshad(num//10,res+num%10)

num1=int(input("Enter a Number:"))
if num1%harshad(num1)==0:
    print("Harshad Number")
else:
    print("not harshad number")