n, k = map(int, input().split())
arr = []
for i in range(1, int(n)+1):
    if (n%i == 0):
        arr.append(n//i)
try:
    print(arr[-k])
except IndexError:
    print(0)
