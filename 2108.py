import sys
from collections import Counter

input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
mean = sum(arr)/n
mean = round(mean) + (1 if int(mean)% 2 == 0 and (mean - float(int(mean))) == 0.5 else 0)
print(mean)
print(arr[n//2])
modes = Counter(arr).most_common()
count = modes[0][1]
modes = list(filter(lambda x: x[1] == count, modes))
modes.sort(key=lambda x: x[0])
print(modes[1][0] if len(modes) > 1 else modes[0][0])
print(max(arr)-min(arr))