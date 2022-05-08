l, a, b, c, d = [int(input()) for _ in range(5)]
korean = a//c + (0 if a%c==0 else 1)
math = b//d + (0 if b%d==0 else 1)
print(l - max(korean, math))