n = int(input())
for i in range(n):
    cnt = 0
    for j in input():
        if cnt == -1:
            break
        elif j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
    if cnt == 0:
        print("YES")
    else:
        print("NO")