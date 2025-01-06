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

getmethod()
This Method give the


  






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
