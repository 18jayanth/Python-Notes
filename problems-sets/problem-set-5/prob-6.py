""" 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique """
d={}
key=input("Enter friend's name:")
value=input("Enter his fav language:")
d.update({key:value})
key=input("Enter friend's name:")
value=input("Enter his fav language:")
d.update({key:value})
key=input("Enter friend's name:")
value=input("Enter his fav language:")
d.update({key:value})
key=input("Enter friend's name:")
value=input("Enter his fav language:")
d.update({key:value})
print(d.items())