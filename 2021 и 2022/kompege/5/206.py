def f(n):
    digs = ''.join(sorted(list(str(n))))
    mx = int(digs[-1] + digs[-2])
    i = digs.rfind('0')
    mn = int(digs[i + 1:i + 3])
    return mx - mn


c = 0

for i in range(800, 901):
    if f(i) == 30: c += 1

print(c)
