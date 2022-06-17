A = set()
P = set(range(2, 20+1, 2))
Q = set(range(3, 30+1, 3))


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (p <= a) or ((not a) <= (not q))


for i in P | Q:
    if not f(i):
        A.add(i)


print(len(A))
