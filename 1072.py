x, y = map(int, input().split())

z = y*100//x
start = 1
end = x
ans = -1

if z < 99: 
    while start <= end:
        mid = (start+end+1)//2
        if ((y+mid)*100//(x+mid) > z):
            end = mid-1
        else:
            start = mid+1
    ans = mid
    if (y+mid)*100//(x+mid) == z:
        ans += 1

print(ans)