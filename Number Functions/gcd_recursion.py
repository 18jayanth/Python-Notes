def gcd(c,d,res):
    if res<1:
        return res
    if c%res==0 and d%res==0:
        return res
    return gcd(c,d,res-1)

a=4
b=6
res1=(a if a<b else b)
print(gcd(a,b,res1))