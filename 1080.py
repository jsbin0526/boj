import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cnt = 0

def flip(x, y): 
    for i in range(3):
        for j in range(3):
            a[y+i][x+j] = 1 - int(a[y+i][x+j])


if (n < 3 or m < 3) and a != b : 
    cnt = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                flip(j, i)
                cnt += 1

if cnt > -1 and a != b:
    cnt = -1

print(cnt)