with open('26-87.txt') as f:
    N = int(f.readline())
    d1,d2 = dict(), dict()
    for _ in range(N):
        t = f.readline().split()
        x,y = int(t[0]), int(t[1])
        if t[2] == '#0000FF': d1[x] = d1.get(x, set()) | {y}
        if t[2] == '#00FF00': d2[x] = d2.get(x, set()) | {y}
m,r = set(), dict()
for _ in sorted(d1.keys()):
    row, t = _ , sorted(d1[_])
    t2 = sorted(d2[row]) if row in d2.keys() else []
    for i1,i2,i3 in zip(t,t[1:],t[2:]):
        if (i3+2 in t and i3+3 in t and i3+4 in t) and (i3+1 not in t and i3+1 in t2):
            m |= {(row,i3+1)}
for i1,i2 in m: r[i1] = r.get(i1, 0) + 1
print(len(m),max(sorted(r.keys(),reverse=1), key=r.get))
