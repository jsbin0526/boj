import math

n = int(input())
matrix = [[" " for i in range(n)] for j in range(n)]

def star(n, x, y):
    if n == 1:
        matrix[y][x] = "*"
        return
    else:
        exp = math.log(3, n)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(n//3, x+j*n//3, y+i*n//3)
star(n, 0, 0)
for i in range(n):
    print("".join(matrix[i]))