import sys

input = sys.stdin.readline

x, y = map(int, input().split())
while ((x, y) != (0, 0)):
    print("Yes" if x > y else "No")
    x, y = map(int, input().split())