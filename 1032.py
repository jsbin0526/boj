import sys
input = sys.stdin.readline

n = int(input())
arr = list(input())
for _ in range(n-1):
    s = input()
    for i in range(len(arr)):
        if arr[i] == s[i]:
            arr[i] = s[i]
        elif arr[i] == '?':
            pass
        else:
            arr[i] = '?'
print(*arr, sep='')