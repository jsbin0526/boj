curr_hour, curr_min = list(map(int, input().split()))
time = int(input())
res_min = (curr_min + time) % 60
res_hour = (curr_hour + ((curr_min+time)//60)) % 24
print(res_hour, res_min)