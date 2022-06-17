A = set()
P = set(range(1, 6+1))
Q = {3, 5, 15}


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (not a) <= ((not p and q) or not q)


for i in P | Q:
    if not f(i):
        A.add(i)


print(len(A))
