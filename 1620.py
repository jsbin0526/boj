import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    s = input()[:-1]
    dic[i] = s
    dic[s] = i
for _ in range(m):
    q = input()[:-1]
    if q[0].isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])
