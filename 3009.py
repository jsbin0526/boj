x, y = [0 for _ in range(3)], [0 for _ in range(3)]
for i in range(3):
    x[i], y[i] = map(int, input().split())
if x[0] == x[1]:
    a = x[2]
elif x[0] == x[2]:
    a = x[1]
else:
    a = x[0]

if y[0] == y[1]:
    b = y[2]
elif y[0] == y[2]:
    b = y[1]
else:
    b = y[0]
print(a, b)