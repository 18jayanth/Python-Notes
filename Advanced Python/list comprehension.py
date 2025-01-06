mylist=[1,2,3,4,5]
"""squaredlist=[]
for i in mylist:
    squaredlist.append(i*i)
print(squaredlist) # 1 4 9 16 25"""
#This can be simplified
squaredlist=[i*i for i in mylist]
print(squaredlist) # same result