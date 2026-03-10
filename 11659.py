import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sums = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sums[j] - prefix_sums[i - 1])