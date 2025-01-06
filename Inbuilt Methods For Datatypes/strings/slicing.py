# string is immutable means once string is created u cannot change it
a="Jayanth"
#string slicing
d=a[0:2] #ja
print(d)
d=a[0:] #jayanth
print(d)
d=a[-1:] #h
print(d)
d=a[-1:-5]
print(d)
d=a[2]
print(d) #y
d=a[-7:]
print(d) #jayanth
#slicing with skip value
a="jayanth"
print(a[0:7:2]) #jynh