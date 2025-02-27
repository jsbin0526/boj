def count_soinsu(n):
    count = 0
    i = 0
    while i < len(primes) and n > 1:
        prime = primes[i]
        if n%prime == 0:
            n //= prime
            count += 1
        else:
            i += 1
    return count


a, b = map(int, input().split())

primes = [True for _ in range(b+1)]
primes[0], primes[1] = False, False

for i in range(2, b+1):
    if primes[i]:
        for j in range(i*2, b+1, i):
            primes[j] = False

primes = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(primes))))

result = 0
for i in range(a, b+1):
    if count_soinsu(i) in primes:
        result += 1

print(result)
