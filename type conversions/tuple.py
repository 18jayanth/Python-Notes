
a=(1,2,2,3) # 1)tuple can contain duplicates
print(a) #2)tuple is ordered datatype
# a[2]=3 3)tuple is immutable datatype
print(a[2]) #2 4)tuple can have indexing
a=(1,3.2,True,3+4j,'abc',['abc'],{'abc'},{'a':'b'})
print(a) #5) is heterogenous but allows homogenous data also
#conversions
#int to tuple
#print(tuple(3)) # 'int' object is not iterable

#float to tuple
#print(tuple(3.2)) #'float' object is not iterable

#bool to tuple
#print(tuple(True)) #'bool' object is not iterable

#complex to tuple
#print(tuple(3+2j)) #'complex' object is not iterable

#str to tuple
print(tuple('abc')) # ('a','b','c')
print(tuple('1')) # ('1',)
#list to tuple 
print(tuple([1,2,3,4])) #(1,2,3,4)
#tuple to tuple
print(tuple((1,2,3,4))) #(1,2,3,4)
#set to tuple
print(tuple({1,2,3,4})) #(1,2,3,4)
#dict to tuple
print(tuple({(1,2,3):2,'123':4})) #((1,2,3),'123') only keys

