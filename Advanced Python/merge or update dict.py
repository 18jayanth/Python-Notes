#New operators | and |= allow for merging and updating dictionaries.
dict1={1:"a",2:"b"}
dict2={3:"c",4:"d"}
merged=dict1|dict2
print(merged)
#we can access more than one file at a time
with (
 open('file1.txt') as f1,
 open('file2.txt') as f2
):
    f1.close()
    f2.close()
