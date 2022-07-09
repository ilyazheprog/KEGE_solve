from itertools import *


def f(x):
    P = 10 <= x <= 15
    Q = 5 <= x <= 20
    R = 15 < x <= 25
    A = a1 <= x <= a2
    return ((not (A)) <= P) != (Q <= R)


Ox = [i / 4 for i in range(200 * 4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(round(min(m)))
