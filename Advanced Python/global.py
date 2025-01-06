"""a=89 # global variable
def func():
    a=3
    print(a)
func() # 3
print(a) #89"""
a=10
def func():
    global a # this keyword changes local to global
    a=3
    print(a)
func() # 3
print(a) #3