a={"jayanth":100,"Rutwik":99,"mukesh":98}
print(a) 
'''There are Three Methods To add values in the Dictionary
#1)    Vn[key]=value  '''
a["sushma"]=97 #insertion
print(a) #{jayanth: 100, rutwik: 99, mukesh: 98, sushma: 97}

'''2)   Using Update Function
This Function is used to add multiple key value pairs to the dictionary
It takes only sequence and length of each item in sequence must be 2 
It Returns None
vn.update(sequence) '''
d={}
d.update('abcd') #error its a sequence but length of element is only one,it must be 2
d.update([1,2,3,4]) #error its a sequence but elements are single value datatype we cant find length of it
d.update(['16','25','34'])
print(d) # {'1':'6','2':'5','3':'4'}
d.update([[33,44],[22,33],[11,22]]) 
print(d) # {'1':'6','2':'5','3':'4',33:44,22:33,11:22}
d={}
d.update(['ab',[44,55],[[3,4],99]) #error a list cant be a key to a dictionary 
#but the earlier elements will be stored
print(d) #{'a':'b',44:55}
d.update('ab') #error element has length 1 but 2 is required
d.update('ab,) 
print(d) #{'a':'b',44:55,'a':'b'}  =  {'a':'b',44:55}
d.update({'a1',(33,22),'42'})
print(d) # {'a':'1',44:55,33:22,'4':'2'}

''' getmethod()
1)This Method give the value for a key which is given as argument
2)If the given key is not available in dictionary get method gives default value
3)If default value not given,get  method gives None
3)It returns the value
Syntax:Vn.get(key) 
Vn.get(key,defaultvalue) '''
D={'a':1,44:55,33:22}
print(D.get('a')) #1
print(D.get(420)) #NOne
print(D.get(420,200)) # 200

'''
3)Setupdate method():
1)This Method give the value for a key which is given as argument
2)If the given key is not available in dictionary get method gives default value
3)If default value not given,setdefault method gives None and returns new key value pair to dictionary
3)It returns the value
'''
Syntax: Vn.setdefualt(key) 
Vn.setdefault(key,defaultvalue) 

D={'a':1,44:55,33:22}
print(D.get('a')) #1
print(D.get(420)) #N0ne
print(D) #{'a':1,44:55,33:22,420:None}
print(D.get(320,120) #120


Remove Methods

1)pop()
This method is used to remove single key value pair from dictionary
If key is not available pop will return default value
IF default is not given pop will return error
pop returns value for the given key
Syntax:Vn.pop(key)
Vn.pop(key,default)

D={'name':'jayanth','age':18}
D.pop('age') #18
print(D) #D={'name':'jayanth'}
D.pop('gender') #error
D.pop('gender','male') #'male

2)popitem()
This method is used to remove  last key value pair from dictionary
popitem returns the last key-value pair in the form of tuple
syntax:vn.popitem()
D={"pushpa2":"1700CR","KGF2":"1100CR","BB2":"1800CR"}
D.popitem() #{"BB2":"1800CR"}

3)clear()
This method removes all key-value pairs from dictionary
This method returns None
Syntax:varn.clear()
D={'a':'b','b':'c'}
D.clear()
D #{}

keys()
This method gives all the keys from dictioanary
Return type of keys method is list but it represents as dict_keys
Syntax:Vn.keys()
D={'a':'b','c':'d'}
D.keys() #dict_keys(['a','c'])

values()
This method gives all the values  from dictioanary
Return type of values  method is list but it represents as dict_values
Syntax:Vn.values()
D={'a':'b','c':'d'}
D.values() #dict_values(['b','d'])

items()
This method gives all the key value pairs in a list and each key value pair stored in a tuple  

Syntax:Vn.items()
D={'a':'b','c':'d'}
D.items() #dict_items([('a':'b'),('c':'d']))

fromkeys
This method is used to create multiple key value pairs with a common value
This method represents keys in a sequence 
No value given default value is NOne
syntax: {}.fromkeys(keys as sequence,value)

{}.fromkeys('pqrs',20)
{'p':20,'q':20,'r':20,'s':20}

{}.fromkeys({4,2,0,'e',(44,55)})
{4:None,2:None,0:None,'e':None,(44,55):None}

{}.fromkeys({'a':4,'b':24,'c':420},48)
{'a':48,'b':48,'c':48}








  






a["jayanth"]=98 #updation

print(a) #jaya 98, rut 99, muk 98, sush 97
print(a.pop("jayanth")) #98
print(a) #rutwik 99, mukesh 98,sushma 97
print(a.popitem()) #sushma 97
print(a) #rutwik 99,mukesh 98
#checks if a key present in dict or not
is_present="jayanth" in a
print(is_present) #false
#checks if a key not present in dict or not
is_notpresent="jayanth" not in a
print(is_notpresent) #True
b=a.copy()
print(b) #rut 99, muk 98
b.update({"jayanth":99,"Sushma":96})
print(b) # rut 99, muk 98,jaya 99, sus 96
#getting the value
value1=b.get("Sushma")
print(value1) #96
value2=b.get('vidya',90)
print(value2) #90 it updates and gives
print(b.get("ramesh")) #none
#print(b["ramesh"]) # it gives error
print(b.clear()) #none it clears entire dictionary
d={}
print(d) #empty dictionary
#print(d.update(('ab'))) dictionary update sequence element #0 has length 1; 2 is required
print(d.update(('ab',))) #none
print(d) #{'a': 'b'}
