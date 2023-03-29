import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append([True if i == 'Y' else False for i in input()[:-1]])

friends = [set([]) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]:
            friends[i].add(j)
            for k in range(n):
                if a[j][k] and i != k:
                    friends[i].add(k)

counts = map(lambda x: len(x), friends)
print(max(counts))