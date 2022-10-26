t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance_pow = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if r1 < r2: r1, r2 = r2, r1

    if (distance_pow == 0):
        if (r1 == r2):
            print(-1)
        else: 
            print(0)
    elif ((r1 - r2) ** 2 < distance_pow < (r1 + r2) ** 2):
        print(2)
    elif (distance_pow == (r1 - r2) ** 2 or distance_pow == (r1 + r2) ** 2):
        print(1)
    else:
        print(0)