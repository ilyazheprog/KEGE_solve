f = open("../../files/kompege/17/1993.txt")
a = [int(_) for _ in f]

good = [x + y for x, y in zip(a, a[1:])
        if (x + y) % 3 == 0 and (x + y) % 6 != 0 and
        abs(x * y) % 10 == 8]
print(len(good), max(good))
