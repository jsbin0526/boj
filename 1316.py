import sys

input = sys.stdin.readline

n = int(input())
li = [0 for i in range(26)]
cnt = 0
for i in range(n):
    li = [0 for i in range(26)]
    is_group = True
    prev = ""
    for s in input().rstrip():
        if prev != "":
            if prev != s:
                if li[ord(s) - 97] != 0:
                    is_group = False
                    break
                else:
                    li[ord(prev) - 97] = -1
            else:
                li[ord(s) - 97] += 1
        prev = s
    if is_group: cnt += 1
print(cnt)
