s={1,2,3,4}
s.add(5)
print(s) # 1 2 3 4 5 
s.update([6,7,8]) # {1 2 3 4 5 6 7 8}
print(s)
s.update((9,10)) # {1 2 3 4 5 6 7 8 9 10}
print(s)
s.update({11,12}) # {1 2 3 4 5 6 7 8 9 10 11 12}
print(s)
s.update({13:14}) # {1 2 3 4 5 6 7 8 9 10 11 12 13}
print(s)
s.update('abcd') #{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'd', 'b', 'a', 'c'}
print(s)
#s.update(1) 'int' object is not iterable
s.update(1,2) #TypeError: 'int' object is not iterable
s.remove(4)
print(s) # 1 2 3 5
s.pop()
print(s) # 2 3 5 removes one element randomly gives error if set is empty
s1={1,2,3}
s2={3,4}
s_union=s1.union(s2)
print(s_union) # 1 2 3 4
s_intersect=s1.intersection(s2)
print(s_intersect) # 3
s_diff=s1.difference(s2)
print(s_diff) # 1 2
sy_diff=s1.symmetric_difference(s2)
print(sy_diff) #  1 2 4 gives values other than common
print(s1.issubset(s2)) # s1 not a subset of s2
print(s1.issuperset(s2)) # s1 is not superset
s_copy=s.copy()
print(s_copy) # 2 3 5 
#updating sets
s1={1,2,5}
s2={3,4}
s1.update(s2)
print(s1) # 1 2 3 4 5 updates s1
s1.intersection_update(s2)
print(s1) #  3 4
s1={1,2,3}
s2={1,2}
s1.difference_update(s2)
print(s1) # 3
s1.symmetric_difference_update(s2)
print(s1) # 1 2 3
print(s1.clear()) #None