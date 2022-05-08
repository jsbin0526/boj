d, h, w = map(int, input().split())
x = (d * d/(h * h + w * w))**0.5
print(int(x * h), int(x * w))