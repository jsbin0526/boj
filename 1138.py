"""
pseudo code

"""

n = int(input())
left_list = list(map(int, input().split()))
height_list = [i for i in range(n)]
result = [None for _ in range(n)]

for i in range(n):
    result[height_list.pop(left_list[i])] = i+1

print(*result, sep=" ")