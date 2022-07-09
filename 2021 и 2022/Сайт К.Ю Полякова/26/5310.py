screen = [[0] * 10_001 for _ in range(10_001)]
pix = {}
count = 0

f = open('../../files/Polyakov/26/5310.txt')
n = int(f.readline())

for _ in range(n):
    s, p, c = f.readline().split()
    s, p = map(int, (s, p))
    screen[s][p] = c

for i in range(10_001):
    s = screen[i]
    for j in range(3, 10_001 - 3):
        if s[j] == '#00FF00' and \
                all(p == '#0000FF'
                    for p in [s[j - 3], s[j - 2], s[j - 1],
                              s[j + 1], s[j + 2], s[j + 3]]):
            pix[i] = pix.get(i, 0) + 1
            count += 1
k = max(pix, key=lambda x: (pix[x], x))
print(count, k)
