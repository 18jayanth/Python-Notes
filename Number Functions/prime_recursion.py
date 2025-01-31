def prime(num, val=2):
    if val >= int(num ** 0.5) + 1:
        return 1

    if num % val == 0:
        return 0

    return prime(num, val + 1)


num = int(input("Enter a number:"))

if num <= 1:
    print("not prime")
else:
    if prime(num):
        print("prime")
    else:
        print("not prime")