import sys
input = sys.stdin.readline

def is_valid(x, y, j, i):
    if x+j < 0 or x+j > 7 or y+i < 0 or y+i > 7:
        return False
    return True


king, stone, n = input().split()
board = [[0 for _ in range(8)] for __ in range(8)]
king = [ord(king[0])-65, int(king[1])-1]
stone = [ord(stone[0])-65, int(stone[1])-1]
n = int(n)
for _ in range(n):
    command = input()[:-1]
    x, y = 0, 0
    if "R" in command:
        x = 1
    elif "L" in command:
        x = -1
    if "B" in command:
        y = -1
    elif "T" in command:
        y = 1
    if is_valid(king[0], king[1], x, y):
        if king[0]+x == stone[0] and king[1]+y == stone[1] and is_valid(stone[0], stone[1], x, y):
            stone[0] += x
            stone[1] += y
        if king[0]+x != stone[0] or king[1]+y != stone[1]:
            king[0] += x
            king[1] += y

print(chr(king[0]+65)+str(king[1]+1))
print(chr(stone[0]+65)+str(stone[1]+1))
