s = []
n, m = map(int, input().split())

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)