import sys
input = sys.stdin.readline

max_num = 999_998

eratosthenes = [False, False] + [True] * (max_num-1)
for i in range(2, max_num):
    if eratosthenes[i]:
        for j in range(2*i, max_num+1, i):
            eratosthenes[j] = False
for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n//2-1):
        if eratosthenes[n//2+i] and eratosthenes[n//2-i]:
            count += 1
    print(count)
