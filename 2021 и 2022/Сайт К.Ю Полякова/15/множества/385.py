A = set()
P = {1, 3, 7}
Q = set(range(1, 6+1)) - {3}


def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return ((not a) <= (not p)) or not q and p


for i in P | Q:
    if not f(i):
        A.add(i)


print(len(A))
