import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    max_div = 1
    for i in range(2, max(a, b)+1):
        if a%i == 0 and b%i == 0:
            max_div = i
    print(a*b//max_div)
