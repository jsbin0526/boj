n, k = map(int, input().split())
count = 0

for i in range(1, 10000000):
    n_copy = n
    need = 1
    while n_copy > 1:
        if n_copy%2 != 0:
            need += 1
        n_copy //= 2
    if need <= k:
        print(count)
        break
    else:
        n += 1
        count += 1