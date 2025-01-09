""" The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it. """
f=open("File Management/file.txt")
print(f.read())
f.close()