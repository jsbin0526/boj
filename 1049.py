import sys
input = sys.stdin.readline

n, m = map(int, input().split())
six, one = 1000, 1000
for _ in range(m):
    a, b = map(int, input().split())
    if a < six:
        six = a
    if b < one:
        one = b

if six < one:
    print(n//6*six+(six if n%6 else 0))
elif six > one*6:
    print(n*one)
else:
    sum = 0
    while n > 0:
        if n > 5:
            sum += six
            n -= 6
        else:
            sum += min(six, one*n)
            n = 0 
    print(sum)