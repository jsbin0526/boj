import sys
input = sys.stdin.readline
n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort()
sum = 0
for i in range(n):
    max = 0
    idx = 0
    for j in range(len(b)):
        if b[j] > max:
            max = b[j]
            idx = j
    sum += a[i] * max
    b.pop(idx)
print(sum)