f = open("../../files/kompege/17/1970.txt")
a = [int(_) for _ in f]

good = [x + y for x, y in zip(a, a[1:]) if x % 3 == 0 or y % 3 == 0]
print(len(good), max(good))
