import sys

input = sys.stdin.readline

def sum_of_withdraw(li):
    ret = 0
    for i in range(len(li)):
        ret += sum(li[:i+1])
    return ret

n = int(input())
li = sorted(map(int, input().split()))
print(sum_of_withdraw(li))