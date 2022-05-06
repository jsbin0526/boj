import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = [0 for _ in range(n + 1)]
    if n > 3:
        li[1] = 1
        li[2] = 2
        li[3] = 4
        i = 4
        while i <= n:
            li[i] = li[i-1] + li[i-2] + li[i-3]
            i += 1
        print(li[n])
    else:
        print(2**(n-1))        