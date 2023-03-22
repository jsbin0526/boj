def get_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
gcd = get_gcd(a1*b2 + a2*b1, b1*b2)

print((a1*b2+a2*b1)//gcd, b1*b2//gcd)