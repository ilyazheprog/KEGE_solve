f = open("../../files/kompege/17/1995.txt")
a = [int(_) for _ in f]

good = [(x + y) // 2 for x, y in zip(a, a[1:])
        if (x + y) % 2 == 0 and abs(x + y) % 10 != 6]
print(len(good), max(good))
