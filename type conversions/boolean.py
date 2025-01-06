a=True
print(type(True))
print(bool()) # False
# 0,0.0.False,0j,'',[],{},(),set(),dict(),None boolean values are False, everything else True
# int to boolean
print(bool(0)) # False
print(bool(1))
# float to boolean
print(bool(0.0)) # False
print(bool(3.2)) # True
#boolean to boolean
print(bool(False)) # False
print(bool(True)) # True
#complex to boolean
print(bool(0j)) # False
print(bool(3+2j)) # True
#string to boolean
print(bool('')) # False
print(bool('123')) # True
#list to boolean
print(bool([])) # False
print(bool([1,2,3])) # True
#tuple to boolean
print(bool(())) # False
print(bool((1,2,3))) # True
#set to boolean
print(bool(set())) # False
print(bool({1,2,3})) # True
#dict to boolean
print(bool()) # False
print(bool({1:2,3:4})) #True

