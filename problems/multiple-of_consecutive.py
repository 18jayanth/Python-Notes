num=int(input("Enter a Number:"))
p1=0
p2=1
while p1*p2<=num:
    if p1*p2==num:
        print(f"{p1},{p2} are consecutive factors to num")
        break
    p1+=1
    p2+=1
else:
    print(f" {p1},{p2} are not consecutive factors to num")
