import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lengths = sorted([int(input()) for _ in range(k)])

start, end =  1, lengths[-1] - lengths[0]
init_val = n // k + (1 if n % k != 0 else 0)
start, end = max(1, lengths[0] // init_val), lengths[-1]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for length in lengths:
        count += length // mid
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)