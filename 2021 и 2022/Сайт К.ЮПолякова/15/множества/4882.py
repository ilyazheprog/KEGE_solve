A = set()
P = set(range(1, 4+1))
Q = set(range(1, 6+1))


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (not a) <= (not p or not q)


for i in P | Q:
    if not f(i):
        A.add(i)


print(len(A))
