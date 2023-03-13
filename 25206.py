import sys
input=sys.stdin.readline

sum = 0.0
dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}
count = 0.0
for _ in range(20):
    arr = input().split()
    if arr[2] == 'P':
        pass
    elif arr[2] == 'F':
        count += float(arr[1])
    else:
        sum += (dict[arr[2][0]] + (0.5 if arr[2][1] == '+' else 0)) * float(arr[1])
        count += float(arr[1])
print(f'{round(sum/count, 6)}')