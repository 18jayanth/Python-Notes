
a=40 # it is an integer
print(int()) # 0
print(a) #40
print(type(a))
# int to int
print(int(6)) #6
#float to int
print(int(3.99)) # 3
#boolean to int
print(int(True)) # 1
#complex to int
# print(int(3+4j)) # error 
#string to int
# print('ab123') # error
# print(int('123')) #123 it should only have numbers to convert not in ' .'
# print(int('3.12')) # it should only have numbers to convert not even '.'
# print(int([1,2,3,4])) # cannot convert list to int
# print(int((1,2,3,4))) #cannot convert tuple  to int
# print(int({1,2,3,4})) # cannot convert set to int
# print(int({1:2,3:4})) # cannot convert dict to int
print(int('1000',2)) # 8
print(bin(8).replace('0b','')) #1000
