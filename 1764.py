import sys
input = sys.stdin.readline

n, m = map(int, input().split())
no_hear = set([input()[:-1] for _ in range(n)])
no_see = set([input()[:-1] for _ in range(m)])
no_hear_no_see = no_hear.intersection(no_see)
print(len(no_hear_no_see))
print(*sorted(list(no_hear_no_see)))
