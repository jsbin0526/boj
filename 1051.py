import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(input())[:-1])

max_num = 1

for y in range(n):
    for x in range(m):
        for i in range(1, min(n-y, m-x)):
            if arr[y][x] == arr[y][x+i] == arr[y+i][x] == arr[y+i][x+i]:
                if (i+1)**2 > max_num:
                    max_num = (i+1)**2
print(max_num)