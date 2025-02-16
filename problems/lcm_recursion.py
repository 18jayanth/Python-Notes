def lcm(c,d,res):
    if res>a*b:
        return res
    if res%a==0 and res%b==0:
        return res
    return lcm(a,b,res+1)
    pass
a=15
b=6
res1=(a if a>b else b)
print(lcm(a,b,res1))
