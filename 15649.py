import sys

s = []
n, m = map(int, input().split())
visited = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False
    
dfs()