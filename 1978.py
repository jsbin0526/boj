def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True


n = int(input())
cnt = 0
li = filter(lambda x: x!= 1, map(int, input().split()))
for i in li:
    if is_prime(i):
        cnt += 1
print(cnt)
