import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for nx in adj[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)