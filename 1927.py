import heapq
import sys

input = sys.stdin.readline
n = int(input())
min_heap = []

for _ in range(n):
    calc = int(input())
    if calc == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, calc)
