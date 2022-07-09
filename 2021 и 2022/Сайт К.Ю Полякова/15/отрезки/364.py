from itertools import *


def f(x):
    P = 20 <= x <= 50
    Q = 10 <= x <= 60
    A = a1 <= x <= a2
    return (P <= A) and (A <= Q)


Ox = [i / 8 for i in range(1, 500 + 1)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(round(max(m)))
