import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

grid = [list(map(int, input().strip())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    count += 1
    return count

complex_count = 0
complex_sizes = []
for i in range(n):
    for j in range(n):
        if grid[j][i] == 1 and not visited[j][i]:
            size = bfs(i, j)
            complex_sizes.append(size)
            complex_count += 1

print(complex_count)
print(*sorted(complex_sizes), sep='\n')