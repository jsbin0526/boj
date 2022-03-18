s = input()
res_list = []
for i in map(chr, range(97, 123)):
    try:
        res_list.append(s.index(i))
    except ValueError:
        res_list.append(-1)
print(" ".join(list(map(str, res_list))))