def f(n):
    b = f"{n:08b}"
    b = b.replace('0', '*').replace('1', '0').replace('*', '1')
    return int(b, 2) + 1


for i in range(1, 128):
    if f(i) == 221:
        print(i)
        break
