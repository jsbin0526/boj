import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(input().split())
b = set(input().split())
print(len((a.difference(b)).union(b.difference(a))))