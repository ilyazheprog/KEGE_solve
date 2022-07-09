A = set()
P = {1, 12}
Q = set(range(12, 16 + 1))


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (not a) <= (not p and not q)


for i in P | Q:
    if not f(i):
        A.add(i)

print(len(A))
