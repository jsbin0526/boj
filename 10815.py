n = int(input())
cards = set(input().split())
m = int(input())
for s in input().split():
    if s in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")