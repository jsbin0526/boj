import sys

input = sys.stdin.readline

def is_empty(li):
    return not len(li)

def func(stack, command):
    l = len(stack)
    if len(command.split()) == 2:
        stack.append(command.split()[1])
    elif command == "pop":
        print(stack.pop(l - 1) if not is_empty(stack) else -1)
    elif command == "size":
        print(l)
    elif command == "empty":
        print(int(is_empty(stack)))
    else:
        print(stack[l - 1] if not is_empty(stack) else -1)
    return stack

n = int(input())
stack = []
for _ in range(n):
    stack = func(stack, input().rstrip())