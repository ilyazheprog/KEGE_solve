f = open("../../files/kompege/17/1994.txt")
a = [int(_) for _ in f]

good = [x * y for x, y in zip(a, a[1:])
        if x * y > 0 and (x + y) % 7 == 0]
print(len(good), min(good))
