def get_gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
gcd = get_gcd(a, b)
print(a*b//gcd)