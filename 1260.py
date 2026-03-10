import sys
from collections import deque

input = sys.stdin.readline

n, m, start_v = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for edge in edges:
    edge.sort()

def dfs(v):
    visited = [False] * (n + 1)
    stack = [v]
    result = []

    while stack:
        e = stack.pop()
        if visited[e]:
            continue
        visited[e] = True
        result.append(str(e))
        for nv in reversed(edges[e]):
            if not visited[nv]:
                stack.append(nv)

    print(' '.join(result))

def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    result = []

    while queue:
        e = queue.popleft()
        result.append(str(e))
        for nv in edges[e]:
            if not visited[nv]:
                visited[nv] = True
                queue.append(nv)

    print(' '.join(result))

dfs(start_v)
bfs(start_v)