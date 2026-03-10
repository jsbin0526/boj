import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            sx, sy = i, j
            break

dist[sx][sy] = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    queue.append((nx, ny))

bfs(sx, sy)

lines = []
for i in range(n):
    row = []
    for j in range(m):
        if grid[i][j] == 0:
            row.append("0")
        else:
            row.append(str(dist[i][j]))
    lines.append(" ".join(row))
print("\n".join(lines))