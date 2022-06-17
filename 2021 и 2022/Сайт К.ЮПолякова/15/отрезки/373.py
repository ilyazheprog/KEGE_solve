def f(x):
    return (x%a==0) <= ((x%21==0) or (x%35==0))
for a in range(1,1000):
    if all(f(x)==1 for x in range(1,10000)):
        print(a)
        break
