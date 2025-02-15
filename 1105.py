l, r = map(str, input().split())

if l == r:
    print(l.count('8'))
elif len(l) != len(r):
    print(0)
else:
    tmp = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                tmp += 1
        else:
            break
    print(tmp)