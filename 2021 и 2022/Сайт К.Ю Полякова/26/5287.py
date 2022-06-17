# Автор: М. Шагитов

Nfree, N0 = 100, 500

# Nfree, N0 = 3, 2

## ( 0 - если из города Н; 1 - если из другого города ).
def check(x):
    cnt = 0
    for i1,i2 in zip(x,x[1:]):
        if i2 - i1 == Nfree + 1: cnt += 1
    if cnt >= 1: return 1
    else: return 0

tcnt = 0
d0 = dict()
d1 = dict()
with open('26-85.txt') as f:
    N = int(f.readline())
    for _ in range(N):
        x,y,z = map(int, f.readline().split())
        if z == 0:
            d0[x] = d0.get(x, []) + [y]
        if z == 1:
            d1[x] = d1.get(x, []) + [y]
        if x <= 25000 and y <= 25000:
            tcnt += 1
if tcnt == N: print('Good')
ans = [0,0]
good = []
for i in sorted(d0.items()):
    t = sorted(i[1])
    if len(t) >= N0: good += [i[0]]
for i in sorted(d1.items()):
    if i[0] in good:
        t0 = sorted(d0[i[0]])
        t1 = sorted(d1[i[0]])
        if check(t1)==1:
            if all(x not in t0 for x in t1):
                if i[0] >= ans[0]:
                    ans = [i[0],len(t1)]
print(*ans)
