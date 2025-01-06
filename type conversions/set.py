
s={1,23,43,43}

print(s) #{1,43,23} #1)will not allow duplicates if given set will remove 2) unordered
#s={1,3.4,True,3+4j,'abcd',[1,2,3,4],(1,2,3,4),{1,2,3,4},{1:2,3:4}} #cant insert list
#s={1,3.4,True,3+4j,'abcd',(1,2,3,4),{1,2,3,4},{1:2,3:4}} #cant insert set in set
#s={1,3.4,True,3+4j,'abcd',(1,2,3,4),{1:2,3:4}}  #cant insert dict in set
s={1,3.4,True,3+4j,'abcd',(1,2,3,4)}  
#30set is heterogenous datatype but allows only immutable collection datatypes and single valued datatpes
#s[2]='bcd' #4) set dont support indexing
s.add('abc') #5) set is mutable datatype
print(s) # {(1,2,3,4),1,3.4,'abcd','abc',(3+4j)}
print(set()) #set()
#conversions
#int to set
#print(set(1)) #'int' object not iterable
#float to set
#print(set(1.2)) #'float' object not iterable
#bool to set
#print(set(True)) #'bool' object not iterable
#complex to set
#print(set(3+4j))   #'complex' object not iterable
#str to set
print(set('abc')) #('b','c','a')
#list to set
print(set([1,2,3,4])) #{1,2,3,4}
#tuple to set
print(set((1,2,3,4))) #{1,2,3,4}
#set to set
print(set({1,2,3,4})) #{1,2,3,4}
#dict to set
print(set({1:2,3:4})) #{1,3}
#print(set([4,1,([7,2]),(33,22)])) # unhashable list
print(set([4,1,'[7,2]',(33,22)])) #{1,'[7,2]',4,(33,22)}
#print(set([4,1,(33,22,[1,2,3])])) #items in the collection must be immutable
#print(set(([3,2,1],'abcd',420))) # unhashable list
#print(set({'abcd',[3,4,5],(11,22,33)})) #unhashable list
#print(set({'a':43,[12,33]:32})) # unhashable list
#print(set([4,1,(3),({33,22},44)])) #unhashable set


