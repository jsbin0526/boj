import sys

input = sys.stdin.readline

m = int(input())
s = [False] * 20

for _ in range(m):
    cmds = input().split()
    if len(cmds) == 1:
        if cmds[0] == 'all':
            s = [True] * 20
        else:
            s = [False] * 20
    else:
        cmd, x = cmds[0], int(cmds[1]) - 1
        if cmd == 'add':
            s[x] = True
        elif cmd == 'remove':
            s[x] = False
        elif cmd == 'check':
            print(1 if s[x] else 0)
        elif cmd == 'toggle':
            s[x] = not s[x]