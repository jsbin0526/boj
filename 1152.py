s_list = input().split()
while s_list.count("") != 0:
    s_list.remove("")
print(len(s_list))