n, x, y = map(int, input().split())
round = 0
while x != y:
    x = x//2 + x%2
    y = y//2 + y%2
    round += 1
print(round)