s = input().upper()
res_list = []
for i in map(chr, range(65, 91)):
    res_list.append(s.count(i))
print(chr(res_list.index(max(res_list))+65) if res_list.count(max(res_list)) == 1 else '?')