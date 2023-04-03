import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
freq = {}
for i in range(n):
    words.append(input().rstrip())
for i in filter(lambda x: len(x) >= m, words):
    freq.setdefault(i, 0)
    freq[i] += 1
words = sorted(freq.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in words:
    print(i[0])