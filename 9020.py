import sys

input = sys.stdin.readline

MAX_NUM = 9998

primes = [False, False] + [True] * (MAX_NUM-1)
for i in range(2, MAX_NUM+1):
    if primes[i]:
        for j in range(2*i, MAX_NUM+1, i):
            primes[j] = False

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2, MAX_NUM+1):
        if primes[i] and primes[n-i]:
            print(n-i, i)
            break