f = open("../../files/kompege/17/1996.txt")
a = [int(_) for _ in f]

good = [(x + y) // 2 for x, y in zip(a, a[1:])
        if x * y % 2 != 0 and (x + y) // 2 % 7 == 0]
print(len(good), min(good))
