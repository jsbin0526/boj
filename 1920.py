import sys

input = sys.stdin.readline

N = int(input())
N_List = sorted(map(int, input().split()))
M = int(input())
M_List = map(int, input().split())
start = 0
end = len(N_List)-1
ret = 0
for m in M_List:
    while start <= end:
        mid = (start+end)//2
        if m == N_List[mid]:
            ret = 1
            break
        elif m > N_List[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(ret)
    start = 0
    end = len(N_List)-1
    ret = 0