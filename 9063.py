import sys
input = sys.stdin.readline

n = int(input())
x, y = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())

x1, x2, y1, y2 = min(x), max(x), min(y), max(y)
print((x2-x1)*(y2-y1))