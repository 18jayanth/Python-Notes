def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
def strong(num):
    if num==0:
        return 0

    return factorial(num%10)+strong(num//10)
num=145
print('strong number'if strong(num)==num else 'not strong number')