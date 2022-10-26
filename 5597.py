li = [True for i in range(31)]
li[0] = False
for _ in range(28):
    li[int(input())] = False
first = li.index(True)
second = li.index(True, first+1)
print(first)
print(second)