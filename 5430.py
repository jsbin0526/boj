import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    funcs = list(input().strip())
    n = int(input())
    arr = list(input().strip('[]').split(','))
    is_error = False
    for func in funcs:
        if func == 'R':
            arr.reverse()
        elif func == 'D':
            if arr:
                arr.pop(0)
            else:
                print('error')
                is_error = True
                break
    if not is_error:
        print('[' + ','.join(arr) + ']')