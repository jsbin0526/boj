def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)

num_list = list(map(int, input().split()))
min_mul = 2147483647

for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            min_mul = min(min_mul, lcm(lcm(num_list[i], num_list[j]), num_list[k]))

print(min_mul)