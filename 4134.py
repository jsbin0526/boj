import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    while True:
        is_prime = True
        for i in range(2, int(n**(0.5))+1):
            if n%i == 0:
                is_prime = False
                break
        if is_prime and n > 1:
            print(n)
            break
        n += 1
