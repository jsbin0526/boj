import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
print("\n".join(map(str, sorted(arr))))