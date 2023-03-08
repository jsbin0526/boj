import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    arr[i:j+1] = reversed(arr[i:j+1])
print(" ".join(arr))