from itertools import *
def f(x):
    P = 10<=x<=23
    Q = 39<=x<=55
    A = a1<=x<=a2
    return ((not(P)) and A) <= (Q and A)
Ox = [i/4 for i in range(1,300+1)]
m = []
for a1,a2 in combinations (Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(round(max(m)))
