li = [i for i in range(10001)]
for i in range(1, 10001):
    n = i
    res = n
    while (n != 0):
        res += n%10
        n //= 10
    if res <= 10000:
        li[res] = 0
for i in filter(lambda x: x != 0, li):
    print(i)