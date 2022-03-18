x = int(input())
n = 1
while True:
    if n%2 == 1:
        if (x-1)//n == n//2:
            print(str(n-((x-1)%n))+'/'+str(((x-1)%n)+1))
            break
        else:
            n += 1
    else:
        if (x-1)//(n+1) == n//2-1:
            print(str((x-1)%(n+1))+'/'+str(n-(x-1)%(n+1)+1))
            break
        else:
            n += 1