#5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
list1=[3*i for i in range(1,11)]
with open ("table1.txt","w") as f:
    f.write(str(list1))
f.close()