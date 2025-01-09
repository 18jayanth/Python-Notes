""" 1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’."""
f=open("poems.txt")
c=f.read()
if("Twinkle" in c):
    print("The word twinkle is present")
else:
     print("The word twinkle is not present")
f.close()