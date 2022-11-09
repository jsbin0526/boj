import sys
import re

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    a = re.fullmatch('(100+1+|01)+', s)
    if (a and a.string == a.group()):
        print("YES")
    else:
        print("NO")
