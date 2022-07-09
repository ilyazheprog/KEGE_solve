A = set()
P = set(range(2, 12 + 1, 2))
Q = set(range(4, 12 + 1, 4)) | {116}


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return p <= ((q and not a) <= (not p))


for i in P | Q:
    if not f(i):
        A.add(i)

print(sum(A))
