"""3. Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old"""
def generate(n):
    table=""
    for i in range(1,11):
        table+=f"{n}*{i}={n*i}\n"
    with open(f"table/multiply_{n}.txt" , "w") as f:
        f.write(table)
    

    
for i in range(2,20):
    generate(i)
    