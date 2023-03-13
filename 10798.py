import sys
input = sys.stdin.readline
arr = [['' for _ in range(15)] for __ in range(5)]

for i in range(5):
    s = list(input()[:-1])
    for j in range(len(s)):
        arr[i][j] = s[j]
        
    
for i in range(15):
    for j in range(5):
        print(arr[j][i], end='')