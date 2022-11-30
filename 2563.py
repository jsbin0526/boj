import sys

input = sys.stdin.readline

paper = [[False for _ in range(100)] for __ in range(100)]
for _ in range(int(input())):
    l, d = map(int, input().split())
    for i in range(l, l+10):
        for j in range(d, d+10):
            paper[i][j] = True
count = [sum(paper[i]) for i in range(100)]
print(sum(count))