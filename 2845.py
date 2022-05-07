l, p = map(int, input().split())
n = l*p
print(" ".join(map(lambda x: str(int(x)-n), input().split())))