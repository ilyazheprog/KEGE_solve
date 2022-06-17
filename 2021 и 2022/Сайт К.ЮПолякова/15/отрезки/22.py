def f(x): return (x&25!=0) <= ((x&17==0) <= (x&a!=0))
for a in range(1,1000):
    if all(f(x)==1 for x in range(1,10000)):
        print(a)
        break
