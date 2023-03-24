import sys
input = sys.stdin.readline

for _ in range(int(input())):
    quarter, dime, nickel, penny = 0, 0, 0, 0
    n = int(input())
    while n > 0:
        if n > 24:
            quarter += 1
            n -= 25
        elif n > 9:
            dime += 1
            n -= 10
        elif n > 4:
            nickel += 1
            n -= 5
        else:
            penny += 1
            n -= 1
    print(quarter, dime, nickel, penny)
