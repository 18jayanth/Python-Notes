a="jayanth"
length=len(a)
print(length) #7
print(a.endswith("nth")) #true
print(a.swapcase()) #JAYANTH
print(a.startswith("jay")) #true
print(a.capitalize()) #Jayanth
print(a.count("a")) # 2
print(a.find("nth")) #4
print(a.isalpha()) #true
print(a.isdigit()) #false
print(a.isalnum()) #true
print(a.islower()) #true
print(a.isupper()) #false
print(a.replace("jay","vid")) #vidanth
print(a.upper()) #JAYANTH
b="JAYANTH"
print(b.lower()) #jayanth
c=121
print(str(c)) #"121"
d="jayanth is a good boy"
print(d.title()) #Jayanth Is A Good Boy
print(d.split()) #['jayanth', 'is','a','good','boy']
print(d.split("a")) #['j','y','nth is ',' good boy']
print(d.split("a",2)) #['j','y','nth is a good boy']
print(d.replace ("a","b")) #jbybnth is b good boy
print(d.replace("a","b",2)) #jbybnth is a good boy
d=" jayanth is a good boy "
print(d.strip()) #jayanth is a good boy
print(d.lstrip()) #jayanth is a good boy
print(d.rstrip()) # jayanth is a good boy
d="jayanth is a good boy"
print(d.strip('j')) # ayanth is a good boy
print(d.lstrip('j')) # ayanth is a good boy
print(d.lstrip('y')) #jayanth is a good boy
print(d.rstrip('j')) #jayanth is a good boy
print(d.rstrip('y')) #jayanth is a good bo
d="jayanth is a good boy"
#index method is used to find the index of the given character from starting index to ending index
print(d.index("a")) #1
print(d.index("a",2)) #3
print(d.index("a",1,8)) #1
print(d.index("a",1,3)) #1
#rindex method is used to find the index of the given character from ending index to starting index
d="jayanth is a good boy"
print(d.rindex("a")) #11
print(d.rindex("a",2)) #11
print(d.rindex("a",1,8)) #3
print(d.rindex("a",1,3)) #1
#print(d.rindex("a",0,1)) #ValueError: substring not found

#find method is used to find the index of the given character
#  from starting index to ending index
#exactly same as index method but only difference is if the given character
#  is not found it will return -1
d="jayanth is a good boy"
print(d.index("a")) #1
print(d.index("a",2)) #3
print(d.index("a",1,8)) #1
print(d.index("a",1,3)) #1
print(d.find("z")) #-1
print(d.find("z",2)) #-1
#rfind is exactly same as rindex method but only difference is
#  if the given character is not found then it will return -1
d="jayanth is a good boy"
print(d.rfind("a")) #11
print(d.rfind("a",2)) #11
print(d.rfind("a",1,8)) #3
print(d.rfind("a",1,3)) #1
print(d.rfind("a",0,1)) #-1