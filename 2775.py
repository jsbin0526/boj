import sys
input = sys.stdin.readline
p = [[i for i in range(1, 15)] for _ in range(15)]
f = 1
for _ in range(int(input())):
    count = 0
    k, n = int(input())-1, int(input())-1
    for i in range(k-f+2):
        for j in range(14):
            p[f+i][j] = sum(p[f+i-1][:j+1])
        count += 1
    f += count
    print(p[k+1][n])