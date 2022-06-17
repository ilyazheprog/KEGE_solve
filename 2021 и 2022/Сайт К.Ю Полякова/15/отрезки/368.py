a = set()
p = {i for i in range(2,14,2)}
q = {4,8,12,116}
def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return P <= ((Q and (not(A))) <= (not(P)))
for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(sum(a))
