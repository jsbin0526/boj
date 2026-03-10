import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = [(0, 0, 1)]
visited[0][0] = True

while queue:
    x, y, dist = queue.pop(0)
    if x == m - 1 and y == n - 1:
        print(dist)
        break
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, dist + 1))