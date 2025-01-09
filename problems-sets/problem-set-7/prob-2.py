""" 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahuls"] """
l = ["Harry", "Soham", "Sachin", "Rahuls"]
for i in l:
    if(i.startswith('S')):
        print("congrats")
    else:
        print("please get lost")
