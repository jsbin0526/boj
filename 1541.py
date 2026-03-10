import sys

input = sys.stdin.readline

equations = input().split('-')
result = 0

for i in range(len(equations)):
    nums = list(map(int, equations[i].split('+')))
    if i == 0:
        result += sum(nums)
    else:
        result -= sum(nums)

print(result)