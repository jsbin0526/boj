import sys
input = sys.stdin.readline

log = {}
for _ in range(int(input())):
    name, s = input().split()
    if s == "enter":
        log[name] = True
    else:
        del log[name]
print(*sorted(log.keys(), reverse=True), sep="\n")
