dice_list = input().split()
if dice_list[0] == dice_list[1] == dice_list[2] : 
    print(10000 + int(dice_list[0])*1000)
elif dice_list[0] == dice_list[1] :
    print(1000 + int(dice_list[0])*100)
elif dice_list[1] == dice_list[2] :
    print(1000 + int(dice_list[1])*100)
elif dice_list[0] == dice_list[2] :
    print(1000 + int(dice_list[0])*100)
else :
    print(int(max(dice_list))*100)