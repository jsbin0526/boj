import sys

s = []
n, m = map(int, input().split())
visited = [False] * (n+1)

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs(i+1)
        s.pop()
        visited[i] = False
    
dfs(1)