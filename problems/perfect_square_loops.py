def perfect(num):
    for i in range(1,num):
        if i*i==num:
            return "perfect square"
    else:
        return "not perfect square"
        #for inputs int then input
num1=int(input("Enter a number:"))
print(perfect(num1))
