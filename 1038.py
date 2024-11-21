n = int(input())
numbers = []
back = []

def dfs():
    for i in range(10):
        back.append(i)
        if len(back) == 1 or back[-2] > i:
            dfs()
            numbers.append(int(''.join(map(str, back))))
        back.pop()

dfs()
numbers.sort()
print(numbers[n] if n < len(numbers) else -1)