import sys
input = sys.stdin.readline

c, h = map(int, input().split())
top = [x[0]*3600+x[1]*60+x[2] for x in [list(map(int, input().split(':'))) for _ in range(c)]]
bot = [x[0]*3600+x[1]*60+x[2] for x in [list(map(int, input().split(':'))) for _ in range(h)]]
time = [True for _ in range(3600*24)]
for i in top:
    for j in range(i, i+40):
        time[j] = False
for i in bot:
    for j in range(i, i+40):
        time[j] = False
print(sum(time))