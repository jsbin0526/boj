import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = {}
filter = [True for _ in range(n)]

for i in range(n):
    min = 1000
    index = 0
    for j in range(n):
        if (a[j] <= min):
            min = a[j] - 1
            index = j
    a[index] = 1001
    b[index] = i

for i in sorted(b.keys()):
    print(b[i], sep=" ")