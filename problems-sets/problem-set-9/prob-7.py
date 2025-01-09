#7. Write a program to find out the line number where python is present from ques 6.
with open("log.txt") as f:
    content=f.readline()
    if("python" in content):
        print("")