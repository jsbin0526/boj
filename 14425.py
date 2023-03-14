import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string_set = []
for _ in range(n):
    string_set.append(input())
string_set = set(string_set)
strings = []
count = 0
for _ in range(m):
    if input() in string_set:
        count += 1
print(count)