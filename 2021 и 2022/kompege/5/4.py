def f(n):
    b = f"{n:b}"
    for _ in range(2):
        b += f"{b.count('1') % 2}"
    return int(b, 2)


for i in range(1, 10 ** 6):
    if f(i) > 77:
        print(i)
        break
