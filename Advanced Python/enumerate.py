l=["jay","1","abc"]
"""index=0
for item in l:
    print(f" the list with the given index {index} is {item}")
    index+=1
the list with the given index 0 is jay
 the list with the given index 1 is 1
 the list with the given index 2 is abc"""
# this can be easily done using enumerators
for index,item in enumerate(l):
    print(f" the list with the given index {index} is {item}")
    # it gives same result
