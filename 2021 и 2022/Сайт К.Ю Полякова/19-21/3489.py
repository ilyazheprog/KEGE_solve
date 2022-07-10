def f(a, b, c, m):
    if a + b <= 18: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a - 1, b, c + 1, m), f(a, b - 1, c + 1, m)]
    if (a + b) % 2 == 0: h += [f(a // 2, b, c + 1, m), f(a, b // 2, c + 1, m)]
    if (a + b) % 2 != 0: h += [f(a // 2 - a % 2, b, c + 1, m), f(a, b // 2 - b % 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 19
ans = set()
for a in range(100 - 1, 1, -1):
    for b in range(100 - a - 1, 1, -1):
        if (a == b) and (a + b >= 19):
            for m in range(1, 5):
                if f(a, b, 0, m) == 1:
                    if m == 2: ans |= {a, b}
                    break
print(*ans)

# 20
ans = []
for x in range(100 - 1, 1, -1):
    for m in range(1, 5):
        if f(13, x, 0, m) == 1:
            if m == 3: ans += [x]
            break
print(min(ans), max(ans))

# 21
ans = set()
for a in range(100 - 1, 1, -1):
    for b in range(100 - a - 1, 1, -1):
        if (a == b) and (a + b >= 19):
            for m in range(1, 5):
                if f(a, b, 0, m) == 1:
                    if m == 4: ans |= {a, b}
                    break
print(*ans)
