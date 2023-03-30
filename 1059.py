import sys
input = sys.stdin.readline

l, s, n = int(input()), sorted(map(int, input().split())), int(input())
count = 0
for i in range(l):
    if n == s[i]:
        start = n
        end = n
        break
    if l == 1 or n < s[0]:
        start = 0
        end = s[0]
        break
    if n > s[i] and n < s[i+1]:
        start = s[i]
        end = s[i+1]
        break

for j in range(start+1, n):
    for k in range(n, end):
        count += 1
for j in range(n+1, end):
    count += 1
print(count)