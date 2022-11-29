N = int(input())

prime = 2
while (prime ** 2 <= N):
    if (N%prime == 0):
        print(prime)
        N //= prime
    else:
        prime += 1
print(N if N > 1 else "")