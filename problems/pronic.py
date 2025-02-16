num=int(input("Enter a Number:"))
p1=0
p2=1
while p1*p2<=num:
    if p1*p2==num:
        print(f" {num} is a pronic number")
        break
    p1+=1
    p2+=1
else:
    print(f" { num} is not a pronic number")
