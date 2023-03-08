import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]
for _ in range(m):
    i, j, k = map(lambda x: int(x)-1, input().split())
    tmp = []
    tmp.extend(arr[k:j+1])
    tmp.extend(arr[i:k])
    arr[i:j+1] = tmp
print(" ".join(arr))