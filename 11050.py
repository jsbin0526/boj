def fact(n):
    mul = 1
    for i in range(2, n+1):
        mul *= i
    return mul

n, r = map(int, input().split())
print(fact(n)//(fact(r)*fact(n-r)))