from itertools import *


def f(x):
    P = 5 <= x <= 15
    Q = 12 <= x <= 18
    A = a1 <= x <= a2
    return (A <= P) or Q


Ox = [i / 4 for i in range(100 * 4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(round(max(m)))
