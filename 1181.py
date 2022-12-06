import sys

input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    arr.append(input().split())
arr.sort(key=lambda x: int(x[0]))
for i in arr:   
    print(i[0], i[1])