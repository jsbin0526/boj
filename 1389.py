import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

INF = int(1e9)
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
    for j in edges[i]:
        dist[i][j] = 1
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
min_sum = INF
answer = -1
for i in range(1, n + 1):
    curr_sum = sum(dist[i][1:])
    if curr_sum < min_sum:
        min_sum = curr_sum
        answer = i

print(answer)