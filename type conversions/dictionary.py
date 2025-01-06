a={'a':2,'b':3}
print(a) #{'a':2,'b':3}
print(dict()) #{}
#conversions
#int to dict
#print(dict(7)) #'int' object is not iterable
#float to dict
#print(dict(7.2)) #'float' object is not iterable
#bool to dict
#print(dict(True)) #'bool' object is not iterable
#complex to dict
#print(dict(3+2j)) #'complex' object is not iterable
#str to dict
#print(dict('abc')) # error dictionary update sequence element #0 has length 1; 2 is required
#print(dict('abcd')) # ValueError: dictionary update sequence element #0 has length 1; 2 is required
#list to dict
#print(dict([1,2,3,4])) # error cannot convert dictionary update sequence element #0 to a sequence
print(dict([[1,2],[3,4]])) # {1:2,3:4}
print(dict(['ab','cd'])) # {'a':'b','c':'d'}
#tuple to dict
#print(dict((1,2,3,4))) # error dictionary update sequence element #0 has length 1; 2 is required
#set to dict
print(dict({' a',' b'})) # {'':'b'}
#print({'mn',[1,2]}) #TypeError: unhashable type: 'list'
#print(dict({1,2,3,4})) # error cannot convert dictionary update sequence element #0 to a sequence
#dict to dict

print(dict({(1,2,3):2,'123':4})) # {(1,2,3):2,'123':4}
