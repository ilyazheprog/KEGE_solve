from itertools import *


def f(x):
    P = 12 <= x <= 26
    Q = 20 <= x <= 35
    A = a1 <= x <= a2
    return A and (not ((P or Q)))


Ox = [i / 4 for i in range(100 * 4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 0 for x in Ox):
        m.append(a2 - a1)
print(round(max(m)))
