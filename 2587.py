a = []
for _ in range(5):
    a.append(int(input()))
a.sort()
print(sum(a)//len(a))
print(a[2])