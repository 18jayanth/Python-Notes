f=open("File Management/file.txt","r")
"""lines=f.readlines()
print(lines,type(lines)) #it returns a list"""
lines=f.readline()
print(lines) # it returns only one string one line

lines1=f.readline()
while(lines1!=""):
    print(lines1)
    lines1=f.readline() # it will print until there is no next line
f.close()


