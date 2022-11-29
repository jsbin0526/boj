M, N = int(input()), int(input())
find_min = False
sum = 0
is_prime = True
for i in range(M, N+1):
    if i == 1:
        continue
    p = 2
    while(p ** 2 <= i):
        if(i%p == 0):
            is_prime = False
            break
        p += 1
    if not is_prime:
        is_prime = True
        continue
    sum += i
    if not find_min:
        min = i
        find_min = True
if sum == 0:
    print(-1)
else:
    print(sum, min)