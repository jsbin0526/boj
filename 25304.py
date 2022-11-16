import sys

input = sys.stdin.readline

sum = int(input())

for _ in range(int(input())):
    price, amount = map(int, input().split())
    sum -= price * amount
print("Yes") if sum == 0 else print("No")