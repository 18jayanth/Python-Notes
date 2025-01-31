def armstrong(num,res=0):
    length=len(str(num))
    dup=num
    while(num!=0):
        rem=num%10
        res+=rem**length
        num//=10
    if res==dup:
        return "Arm Strong Number"
    else:
        return 'Not Arm Strong Number'
num=int(input('Enter a Number:'))
print(armstrong(num))