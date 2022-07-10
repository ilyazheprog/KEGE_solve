# Неудачный ход any(h)
def f(a, b, c, m):
    if a + b >= 45: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + b, b, c + 1, m), f(a, b + a, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)


# 19
ans = []
for x in range(100 - 1, 1, -1):
    for m in range(1, 5):
        if f(7, x, 0, m) == 1:
            if m == 2: ans += [x]
            break
print(min(ans))


def f(a, b, c, m):
    if a + b >= 45: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + b, b, c + 1, m), f(a, b + a, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# 20
ans = []
for x in range(100 - 1, 1, -1):
    for m in range(1, 5):
        if f(6, x, 0, m) == 1:
            if m == 3: ans += [x]
            break
print(min(ans), max(ans))

# 21
ans = set()
for a in range(100 - 1, 1, -1):
    for b in range(100 - a - 1, 1, -1):
        if a == b:
            for m in range(1, 5):
                if f(a, b, 0, m) == 1:
                    if m == 4: ans |= {a, b}
                    break
print(min(ans))
