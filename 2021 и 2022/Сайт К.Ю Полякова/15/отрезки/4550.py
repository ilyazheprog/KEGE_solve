from itertools import *
def f(x):
    P = 5<=x<=10
    Q = 10<=x<=20
    R = 25<=x<=40
    A = a1<=x<=a2
    return (A <= P) == (Q <= R)
Ox = [i/4 for i in range(200*4) if i!=10]
Ox.remove(10.0)
m = []
for a1,a2 in combinations (Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(round(max(m)))
