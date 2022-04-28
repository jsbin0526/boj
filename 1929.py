import sys

input = sys.stdin.readline().rstrip

m, n = map(int, input().split())
primeList = [True] * (n+1)
primeList[0] = False
primeList[1] = False
for i in range(2, n+1):
    if primeList[i]:
        for j in range(i*2, n+1, i):
            primeList[j] = False
for i in range(m, n+1):
    if primeList[i]: print(i)