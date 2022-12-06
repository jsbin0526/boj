N = int(input())
arr = list(map(int, input().split()))
sort = sorted(set(arr))
dict = {sort[i]: i for i in range(len(sort))}
for i in arr:
    print(dict[i], end=" ")