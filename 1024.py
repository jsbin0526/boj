n, l = map(int, input().split())
while True:
    if l > n+1 or l > 100:
        print(-1)
        break
    if l%2 != 0 and n%l == 0 and n//l >= l//2:
        print(*[i for i in range(n//l-l//2, n//l+l//2+1)])
        break
    elif l%2 == 0 and (n-l//2)%l == 0 and n//l+1 >= l//2:
        print(*[i for i in range(n//l-l//2+1, n//l+l//2+1)])
        break
    l += 1