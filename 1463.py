n = int(input())
li = [0]*(n+1)
for i in range(2, n+1):
    d2, d3 = i//2, i//3
    if (not i%2) and (not i%3):
        li[i] = min(li[i-1], li[d2], li[d3]) + 1
    elif not i%2:
        li[i] = min(li[i-1], li[d2]) + 1
    elif not i%3:
        li[i] = min(li[i-1], li[d3]) + 1
    else:
        li[i] = li[i-1] + 1
print(li[n])
