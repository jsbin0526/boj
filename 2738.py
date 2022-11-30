import sys

input = sys.stdin.readline

c, r = map(int, input().split())
a, b = [], []
for _ in range(c):
    a.append(list(map(int, input().split())))
for _ in range(c):
    b.append(list(map(int, input().split())))
for i in range(c):
    for j in range(r):
        print(a[i][j]+b[i][j], end=" ")
    print()