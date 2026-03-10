from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    visited = [-1] * 100001
    visited[n] = 0
    q = deque()
    q.append(n)

    while (len(q)):
        x = q.popleft()
        if x == k:
            return visited[x]
        
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)

print(bfs(n, k))