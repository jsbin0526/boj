board = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "F" and (i+j)%2 == 0:
            cnt += 1

print(cnt)