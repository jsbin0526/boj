import sys
input = sys.stdin.readline

log = {"ChongChong": True}
for _ in range(int(input())):
    p1, p2 = input().split()
    if log.get(p1, False):
        log[p2] = True
    elif log.get(p2, False):
        log[p1] = True
print(len(log))