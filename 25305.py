k = int(input().split()[1])
print(sorted(map(int, input().split()), reverse=True)[k-1])