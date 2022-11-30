import sys

input = sys.stdin.readline

a = []
m = 0
max_r = 0
max_c = 0

for i in range(9):
    a.append(list(map(int, input().split())))
    arr = a[i][:]
    for j in range(9):
        if arr[j] > m:
            m = arr[j]
            max_r = j
            max_c = i
print(m)
print(max_c+1, max_r+1)