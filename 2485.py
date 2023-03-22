import sys
input = sys.stdin.readline

def get_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
distances = []
last = int(input())

for _ in range(n-1):
    current = int(input())
    distances.append(current-last)
    last = current

gcd = distances[0]
for i in range(1, len(distances)):
    gcd = get_gcd(gcd, distances[i])
print(sum(map(lambda x: x//gcd-1, distances)))