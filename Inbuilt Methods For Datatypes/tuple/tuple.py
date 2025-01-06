a=(1,2,2,3)
# tuples are immutable
print(a)
print(type(a))
d=a.count(2)
print(d) # 2
ab=a.index(2)
print(ab) #1
length=len(a)
print(length) #4
print(max(a)) #3
print(min(a)) #1
print(sum(a)) #8
print(sorted(a)) #gives a sorted list [1,2,2,3]
print(any(a)) # True Returns true if atleast one element
print(all(a)) # True Returns True if all elements are true
m,n,o,p=a
print(m,n,o,p) # unpacking the tuple
#we can also concatenate and repeat
t1=(1,2)
t2=(3,4)
print(t1+t2) #(1,2,3,4)
print(t1*2) #(1,2,1,2)

