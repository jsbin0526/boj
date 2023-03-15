n = int(input())
dic = {}
for s in input().split():
    if dic.get(s) != None:
        dic[s] += 1
    else:
        dic[s] = 1
m = int(input())
for s in input().split():
    if dic.get(s) != None:
        print(dic.get(s), end=" ")
    else:
        print(0, end=" ")