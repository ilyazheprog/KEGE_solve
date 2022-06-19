from itertools import *
def f(x):
    P = 37<=x<=60
    Q = 40<=x<=77
    A = a1<=x<=a2
    return P <= ((Q and (not(A))) <= (not(P)))
Ox = [i/4 for i in range(1,300+1)]
m = []
for a1,a2 in combinations (Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(round(min(m)))
