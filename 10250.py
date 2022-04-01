t = int(input())
for i in range(t):
  h, w, n = map(int, input().split())
  distance = (n-1)//h+1
  if n <= w: floor = 1
  else: floor = n%w
  print(str(floor)+('0' if distance < 10 else '')+str(distance))