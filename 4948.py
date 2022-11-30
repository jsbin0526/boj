import sys

input = sys.stdin.readline

primes = [False, False] + [True] * 246911
for i in range(2, 246913):
    if primes[i]:
        for j in range(2*i, 246913, i):
            primes[j] = False
n = int(input())
while n != 0:
    count = 0
    for i in range(n+1, 2*n+1):
        if primes[i]:
            count += 1
    print(count)
    n = int(input())