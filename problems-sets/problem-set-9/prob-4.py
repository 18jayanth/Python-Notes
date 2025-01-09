"""4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. """
with open("donkey.txt") as f:
    content=f.read()
contentrewrite=content.replace("donkey","#####")
with open("donkey.txt" ,"w") as f:
    f.write(contentrewrite)

 