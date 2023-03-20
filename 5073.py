import sys
input = sys.stdin.readline

pos = []
i = 0
while True:
    pos.append(list(map(int, input().split())))
    lens = pos[i]
    if not lens[0]:
        break    
    else:
        lens.sort()
        if lens[2] >= lens[1] + lens[0]:
            print("Invalid")
        elif lens[0] == lens[1] == lens[2]:
            print("Equilateral")
        elif lens[0] == lens[1] or lens[1] == lens[2] or lens[0] == lens[2]:
            print("Isosceles")
        else:
            print("Scalene")
        i += 1
        