import sys

input = sys.stdin.readline

n, k = map(int, input().split())
li = list(reversed([int(input()) for _ in range(n)]))
cnt = 0
i = 0
while k > 0:
    unit = li[i]
    if unit <= k:
        cnt += k//unit
        k -= k//unit*unit
    else:
        i += 1
print(cnt)