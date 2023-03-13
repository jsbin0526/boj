s = input()
n = len(s)
is_pelindrom = 0
for i in range(n):
    if s[i] == s[n-i-1]:
        is_pelindrom = 1
    else:
        break
print(is_pelindrom)