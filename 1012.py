import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

def dfs(arr, x, y):
    if not arr[y][x]:
        return True
    else:
        arr[y][x] = False
        if x != 0:
            dfs(arr, x-1, y)
        if x != len(arr[0]) - 1:
            dfs(arr, x+1 ,y)
        if y != 0:
            dfs(arr, x, y-1)
        if y != len(arr) - 1:
            dfs(arr, x, y+1)
        return True


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[False for i in range(m)] for j in range(n)]
    count = 0
    for __ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = True
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                dfs(arr, j, i)
                count += 1
    print(count)