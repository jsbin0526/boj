import sys
from math import sqrt

input = sys.stdin.readline

for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    sum = 0
    for __ in range(int(input())):
        x, y, r = map(int, input().split())
        s_to_pl = sqrt((sx-x)**2 + (sy-y)**2)
        e_to_pl = sqrt((ex-x)**2 + (ey-y)**2)
        if s_to_pl < r and e_to_pl < r:
            pass
        elif s_to_pl < r:
            sum += 1
        elif e_to_pl < r:
            sum += 1
    print(sum)
