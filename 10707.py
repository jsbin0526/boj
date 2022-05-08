a, b, c, d, p = [int(input()) for _ in range(5)]
print(min(p * a, b + max((p - c) * d, 0)))