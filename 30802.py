import math

n = int(input())
a = map(int, input().split())
t, p = map(int, input().split())
print(sum(map(lambda x: math.ceil(x/t), a)))
print(n//p, n%p)