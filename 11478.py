s = input()
n = len(s)
arr = []
for i in range(n):
    for j in range(i+1, n+1):
        arr.append(s[i:j])
print(len(set(arr)))
