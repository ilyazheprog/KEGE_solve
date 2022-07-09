from itertools import *


def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not (R))) and (A and (not (P)))


Ox = [i / 4 for i in range(1, 300 + 1)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 0 for x in Ox):
        m.append(a2 - a1)
print(round(max(m)))
