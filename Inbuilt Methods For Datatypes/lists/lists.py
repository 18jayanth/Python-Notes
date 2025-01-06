fruits=["mango","apple","oranges"]
print(fruits)
fruits[0]="almond" # unlike strings are immutable lists can be mutable
print(fruits)
print(fruits[0:2])
""" in strings it is immutable, means whenever there is a function is used to update the string it will give back
a new string old string will be the same but in lists whenever there is any function used to change the lists
list will be changed """
fruits.append('mango')
print(fruits)
l1=[10,50,20,80,0]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,333) #inserting 333 at index 3
print(l1) #80,50,20,333,10,0
#pop function returns the value to be popped at that index
value=l1.pop(3) 
print(value) #333
print(l1) # 80,50,20,10,0
l1.remove(50)
print(l1) # it removed 50   80,20,10,0
l1.extend([30,40])
print(l1) #80,20,10,0,30,40 extends the list
l1.pop(1)
print(l1) #80,10,0,30,40 pops element at a index
index_of_10=l1.index(10)
print(index_of_10) # 1 it gives first occurence of a given element
count_of_30=l1.count(30)
print(count_of_30) # 1 it gives count of a given number
l2=l1.copy()
print(l2) #80,10,0,30,40
#List comprehension
lst=[x*2 for x in range(5)]
print(lst)

