def disarum(num):
    power=len(str(num))
    res=0
    dup=num
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
        power-=1
    if res==dup:
        print("Disarum Number")
    else:
        print("Not disarum number")
num=int(input('Enter a number:'))
disarum(num)