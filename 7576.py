import sys

input = sys.stdin.readline

m, n = map(int, input().split()) # m: rows, n: columns
grid = [list(map(int, input().split())) for _ in range(n)] # 1 if ripe, 0 if unripe, -1 if no tomato
visited = [[False] * m for _ in range(n)]

def bfs(row, col, queue):
    visited[row][col] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    days = -1
    while queue:
        days += 1
        next_queue = []
        for r, c in queue:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    grid[nr][nc] = 1
                    next_queue.append((nr, nc))
        queue = next_queue
    return days

queue = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
if queue:
    count = bfs(queue[0][0], queue[0][1], queue)
else:
    count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            count = -1
            break
    if count == -1:
        break
print(count)