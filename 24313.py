a1, a0 = map(int, input().split())
c, n0 = map(int, (input(), input()))
print(int(c*n0 >= a1*n0+a0 and c >= a1))