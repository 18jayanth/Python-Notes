def lcm(c,d,res):
    while True:
        if res%c==0 and res%d==0:
            return res
        res+=1

a=16
b=9
res1=(a if a>b else b)
print(lcm(a,b,res1))
