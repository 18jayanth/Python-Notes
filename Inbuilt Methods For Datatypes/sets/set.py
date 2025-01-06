set1={1,2,3,4}
#empty set
empty=set()
print(type(empty)) # class set
set2=({1,2,1,"harry"})
print(set2,type(set2)) # 1 2 harry no duplicates are strored
set2.add(5)
print(set2)
# we cannot change any existing element in the set and it does not contain duplicates
#sets are unordered and unindexed

