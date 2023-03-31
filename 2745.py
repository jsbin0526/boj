n, b = input().split()
dec = 0
b = int(b)
for i in range(len(n)):
    if n[i].isalpha():
        x = ord(n[i])-55
    else:
        x = int(n[i])
    dec += x*b**(len(n)-i-1)
print(dec)