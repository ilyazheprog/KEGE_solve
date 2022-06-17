P = set(range(2, 20+1, 2))
Q = set(range(3, 30+1, 3))
A = P | Q


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (a <= (not p)) and ((not q) <= (not a))


for i in P | Q:
    if not f(i):
        A.remove(i)


print(len(A))
