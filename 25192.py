import sys
input = sys.stdin.readline

count = 0
log = {}
n = int(input())
input()
for _ in range(n-1):
    name = input()[:-1]
    if name == "ENTER":
        log.clear()
        continue
    if not log.get(name, False):
        log[name] = True
        count += 1
print(count)