list_of_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
count = 0
len_of_croatia = 0
for i in list_of_alphabet:
    if i in s:
        for j in range(0, len(s)-len(i)+1):
            if s[j:j+len(i)] == i:
                count += 1 if i != 'dz=' else 0
                len_of_croatia += len(i) if i != 'dz=' else 1
print(count+len(s)-len_of_croatia)