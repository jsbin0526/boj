amount = int(input())
for _ in range(amount):
    r, s = input().split()
    print("".join(list(map(lambda x: x*int(r), s))))
