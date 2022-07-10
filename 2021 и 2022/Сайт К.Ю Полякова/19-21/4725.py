def f(s1, s2, s3, c, m):
    if s1 + s2 + s3 >= 71: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s1 + 3, s2, s3, c + 1, m), f(s1, s2 + 3, s3, c + 1, m), f(s1, s2, s3 + 3, c + 1, m),
         f(s1 * 2, s2, s3, c + 1, m), f(s1, s2 * 2, s3, c + 1, m), f(s1, s2, s3 * 2, c + 1, m), ]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 60):
    for m in range(1, 5):
        if f(7, 5, s, 0, m) == 1:
            if m == 4: print(s, end=' ')
            break
