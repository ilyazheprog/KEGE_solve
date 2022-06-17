def f(x):
    return (x%a!=0) <= ((x%21!=0) and (x%35!=0))
ans = []
for a in range(1,1000):
    if all(f(x)==1 for x in range(1,10000)):
        ans += [a]
print(max(ans))
