from math import prod

A = set()
P = {2, 4, 9, 10, 15}
Q = {3, 8, 9, 10, 20}


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (not p == a) <= (q == a)


for i in P | Q:
    if not f(i):
        A.add(i)

print(prod(A))
