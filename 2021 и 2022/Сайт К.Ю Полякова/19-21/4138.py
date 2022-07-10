def f(s, c, m):
    if s == 1: return c % 2 == m % 2
    if c == m: return 0
    h = []
    if s % 2 == 0:
        h += [f(s // 2, c + 1, m)]
    else:
        h += [f(s - 2, c + 1, m)]
    if s % 3 == 0:
        h += [f(s - (2 / 3 * s), c + 1, m)]
    else:
        h += [f(s - 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 40):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            if m == 4: print(s)
            break
