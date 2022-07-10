# Неудачных ход any
def f(t1, t2, t3, c, m):
    if t1 + t2 + t3 >= 73: return c % 2 == m % 2
    if c == m: return 0
    h = [f(t1 + 3, t2, t3, c + 1, m), f(t1, t2 + 3, t3, c + 1, m), f(t1, t2, t3 + 3, c + 1, m),
         f(t1 + 13, t2, t3, c + 1, m), f(t1, t2 + 13, t3, c + 1, m), f(t1, t2, t3 + 13, c + 1, m),
         f(t1 + 23, t2, t3, c + 1, m), f(t1, t2 + 23, t3, c + 1, m), f(t1, t2, t3 + 23, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)


# 19
ans = set()
for s in range(1, 25):
    for m in range(1, 5):
        if f(2, s, 2 * s, 0, m) == 1:
            if m == 2: ans |= {s}
            break
print(min(ans))


def f(t1, t2, t3, c, m):
    if t1 + t2 + t3 >= 73: return c % 2 == m % 2
    if c == m: return 0
    h = [f(t1 + 3, t2, t3, c + 1, m), f(t1, t2 + 3, t3, c + 1, m), f(t1, t2, t3 + 3, c + 1, m),
         f(t1 + 13, t2, t3, c + 1, m), f(t1, t2 + 13, t3, c + 1, m), f(t1, t2, t3 + 13, c + 1, m),
         f(t1 + 23, t2, t3, c + 1, m), f(t1, t2 + 23, t3, c + 1, m), f(t1, t2, t3 + 23, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 20
ans = set()
for s in range(1, 25):
    for m in range(1, 5):
        if f(2, s, 2 * s, 0, m) == 1:
            if m == 3: ans |= {s}
            break
print(min(ans), max(ans))

# 21
ans = set()
for s in range(1, 25):
    for m in range(1, 5):
        if f(2, s, 2 * s, 0, m) == 1:
            if m == 4: ans |= {s}
            break
print(*sorted(ans)[1:])
