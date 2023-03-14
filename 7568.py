import sys
input = sys.stdin.readline

def comparison(a, b):
    return a[0] > b[0] and a[1] > b[1]

n = int(input())
arr = []
ranks = [1 for _ in range(n)]

for i in range(n):
    arr.append(tuple(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        if comparison(arr[i], arr[j]):
            ranks[j] += 1
        elif comparison(arr[j], arr[i]):
            ranks[i] += 1
print(" ".join(map(str, ranks)))