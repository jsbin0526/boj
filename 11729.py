n = int(input())
k = 0
prog = []

def hanoi(n, begin, end, mid):
    global k
    k += 1
    if n == 1:
        prog.append([begin, end])
    else:
        hanoi(n-1, begin, mid, end)
        prog.append([begin, end])
        hanoi(n-1, mid, end, begin)

hanoi(n, 1, 3, 2)
print(k)
for e in prog:
    print(" ".join(map(str, e)))
