
a=3.12
b=3.0
print(type(a)) # float
print(id(a)) # 230187049 memory location
print(float()) # 0.0
#int to float
print(float(3)) #3.0
#float to float
print(float(3.2)) #3.2
#boolean to float
print(float(True)) # 1.0
#complex to float
# print(float(3+2j)) # error
#string to float
print(float('23')) #23.0
print(float('3.2')) #3.2
# print(float('ab.c')) # it should contain only nuumbers and even '.'
#list to float
print(float([3,2,1,4])) # cannot convert list into float
print(float((1,2,3,4))) # cannot convert tuple  into float
print(float({1,2,3,4})) # cannot convert set into float
print(float({1:2,3:4})) # cannot convert dict into float
