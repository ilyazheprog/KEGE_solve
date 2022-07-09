def f(n):
    b = f"{n:b}"
    b = b + '11' if b.count('1') % 2 == 1 else '11' + b
    return int(b, 2)


for i in range(1, 10 ** 6):
    if f(i) > 102:
        print(i)
        break
