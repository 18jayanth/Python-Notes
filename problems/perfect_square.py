num=int(input("Enter a Number:"))
for i in range(1,num+1):
    if i*i==num:
        print("Perfect square")
        break
else:
    print("Not a Perfect square")
