t = int(input())
for _ in range(t):
    n = int(input())
    if n > 1:
        li = [0 for _ in range(41)]
        li[n] = 1
        while n > 1:
            li[n-1] += li[n]
            li[n-2] += li[n]
            n -= 1 
        print(li[0], li[1])
            
    else:
        print(str(1-n), str(n))
