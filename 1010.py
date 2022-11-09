import sys

def factorial(s, e):
    n = 1
    for i in range(s, e+1):
        n *= i
    return n

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 1
    for i in range(1, n+1):
        ans *= m-i+1
        ans //= i 
    print(ans)