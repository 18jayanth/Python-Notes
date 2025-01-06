a="Jayanth"
print(a)
print(type(a)) #str
print(str()) 
# 1)string is ordered
print(a[3]) # a 2)string is indexed
#3)string also can contain duplicates
#4)string contains only homogeneous data
 # a[3]='b' error 5)immutable data
 #Conversions
# int to str
print(str(3))
print(str(0))
# float to str
print(str(3.2))
#boolean to str
print(str(True)) # True
#complex to str
print(str(3+2j)) #(3+2j)
#str to str
print(str('jayanth')) #jayanth
#list to str
print(str([3,4,5]))
print(len(str([3,4,5])))#9 '[' '3' ',' '' '4' ',' '' '5' ']'
print(str([3,'a',63]))
print(len(str([3,'a',63]))) #12 # '[' '3' ',' ' ' ''' 'a' ''' ',' ' ' '6' '3' ']'
a=str([3,'a',63])
print(a[10]) #3
print(a[11]) #]
#tuple to str #similar to list
print(str((1,2,3)))
print(len(str((1,2,3)))) #9 '(' '1' ',' ' ' '2' ',' ' ' '3' ')' 
#set to str #similar to list
print(str({1,2,3})) #9
print(len(str({1,2,3})))#9 '{' '1' ',' ' ' '2' ',' ' ' '3' '}' 
#dixt to str
print(str({1:2,3:4}))
print(len(str({1:2,3:4})))#12 '{' '1' ':' ' ' '2' ',' ' ' '3' ':' ' ' '4' '}'


