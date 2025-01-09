f=open("File Management/file.txt","r")
print(f.read())
f.close()
with open("File Management/file.txt") as f:
    print(f.read())
    #we dont have to explicitly write close function