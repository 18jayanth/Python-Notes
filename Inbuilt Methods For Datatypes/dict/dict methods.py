a={"jayanth":100,"Rutwik":99,"mukesh":98}
print(a)
a["jayanth"]=98 #updation
a["sushma"]=97 #insertion
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