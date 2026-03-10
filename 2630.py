import sys

input = sys.stdin.readline


def recursion(row, column, n, white, blue):
    if n == 1:
        if papers[row][column] == 0:
            white += 1
        else:
            blue += 1
        return white, blue
    color = papers[row][column]
    for i in range(row, row + n):
        for j in range(column, column + n):
            if papers[i][j] != color:
                white1, blue1 = recursion(row, column, n // 2, 0, 0)
                white2, blue2 = recursion(row, column + n // 2, n // 2, 0, 0)
                white3, blue3 = recursion(row + n // 2, column, n // 2, 0, 0)
                white4, blue4 = recursion(row + n // 2, column + n // 2, n // 2, 0, 0)
                return white1 + white2 + white3 + white4, blue1 + blue2 + blue3 + blue4
    if color == 0:
        white += 1
    else:
        blue += 1
    return white, blue

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

white, blue = recursion(0, 0, n, 0, 0)
print(white)
print(blue)