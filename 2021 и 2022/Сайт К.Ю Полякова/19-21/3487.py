def f(a, b, c, m):
    if a + b >= 30: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 19
ans = set()
for a in range(30 - 1, 1, -1):
    for b in range(30 - a - 1, 1, -1):
        if a + b <= 29:
            for m in range(1, 5):
                if f(a, b, 0, m) == 1:
                    if m == 2: ans |= {a, b}
                    break
print(len(ans))

# 20
ans = []
for x in range(30 - 1, 0, -1):
    for m in range(1, 5):
        if f(x, 7, 0, m) == 1:
            if m == 3: ans += [x]
            break
print(min(ans), max(ans))

# 21
ans = []
for x in range(30 - 1, 0, -1):
    for m in range(1, 5):
        if f(1, x, 0, m) == 1:
            if m == 4: ans += [x]
            break
print(max(ans))
