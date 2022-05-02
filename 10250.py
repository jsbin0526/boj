import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
  h, w, n = map(int, input().split())
  distance = (n-1)//h + 1
  floor = (n-1)%h + 1
  fill_num = '0' if distance < 10 else ''
  print(str(floor) + fill_num + str(distance))
