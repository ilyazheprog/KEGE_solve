def f(a, b, c, m):
    if 47 <= a + b <= 59: return c % 2 == m % 2
    if a + b > 59: return c % 2 != m % 2
    if c == m: return 0
    h = [f(a + 2, b, c + 1, m), f(a, b + 2, c + 1, m), f(a * 3, b, c + 1, m), f(a, b * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 41 + 1):
    for m in range(1, 5):
        if f(5, s, 0, m) == 1:
            if m == 3: print(s, end=' ')
            break
