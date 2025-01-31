def gcd(c,d,res):
    while True:
        if c%res==0 and d%res==0:
            return res
        res-=1

a=16
b=32
res1=(a if a<b else b)
print(gcd(a,b,res1))