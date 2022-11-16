import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = list(map(int, input().rstrip().split()))
count = 0
i = 0
dq = deque([i for i in range(1, n+1)])
while (i < m):
    if dq[0] == q[i]:
        dq.popleft()
        i += 1
    else:
        if dq.index(q[i]) < len(dq)-dq.index(q[i]):
            dq.append(dq.popleft())
            count += 1
        else:
            dq.appendleft(dq.pop())
            count += 1
print(count)