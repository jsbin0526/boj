n = int(input())
if n == 1 : print(1)
else :
    layer = 1
    sum = 6
    while True:
        if sum > n-2 :
            print(layer+1)
            break
        else:
            layer += 1
            sum += 6*layer