def f(a, b, c, m):
    if a + b >= 99: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 3, b, c + 1, m), f(a, b * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(1, 91):
    for m in range(1, 4):
        if f(8, b, 0, m) == 1:
            if m % 2 == 0: print(b, m)
            break
