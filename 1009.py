import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    b = (b-1)%4+1
    n = int(str(a)[-1])**b%10 if int(str(a)[-1])**b%10 != 0 else 10
    print(n)
