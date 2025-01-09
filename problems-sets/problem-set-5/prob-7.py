#7. If the names of 2 friends are same; what will happen to the program in problem 6
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
# if there are duplicate keys dict it updates to last key