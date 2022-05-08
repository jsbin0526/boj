h, m, s, t = map(int, input().split() + [input()])
h += t//3600
t -= t//3600*3600
m += t//60
t -= t//60*60
s += t
if s >=60:
    over = s//60
    m += over
    s -= 60*over
if m >= 60:
    over = m//60
    h += over
    m -= 60*over
print(h%24, m, s)
