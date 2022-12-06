import sys

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(i[0], i[1])