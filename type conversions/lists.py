a=[3,4,5,3] #1)list can contain duplicates
print(a) # 2)list is ordered
print(type(a)) # list
print(list()) #[]
#3)list is an heterogenous datatype but allows homogenous also
print(a[2])# 5  4)list has indexing
a[2]='abc'
print(a) # [3,4,'abc',3] 5)list is mutable
#Converting to list
#int to list
#print(list(3)) #'int' object is not iterable

#float to list
#print(list(3.0)) #'float' object is not iterable

#bool to list
#print(list(True)) #'bool' object is not iterable

#complex to list
#print(list(3+2j)) #'complex' object is not iterable

#str to list
print(list('abc')) #['a','b','c']
print(len(list('abc'))) # 3

#list to list
print(list([1,2,3]))#[1,2,3]

#tuple to list
print(list((1,2,3))) #[1,2,3]
print(list((1,))) #[1]

#set to list
print(list({1,2,3,4})) #[1,2,3,4]

 #dict to list
print(list({1:2,3:4})) #[1,3] only keys



