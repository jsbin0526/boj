n, b = map(int, input().split())
n_dec = []
while n > 0:
    mod = n%b
    n //= b
    if mod >= 10:
        mod = chr(mod+55)
    else:
        mod = str(mod)
    n_dec.append(mod)
print("".join(reversed(n_dec)))