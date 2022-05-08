n = int(input())
a, b, c = 0, 0, 0
if not n%10:
    while n > 0:
        if n >= 300:
            n -= 300
            a += 1
        elif n >= 60:
            n -= 60
            b += 1
        else: 
            n -= 10
            c += 1
    print(a, b, c)
else:
    print(-1)