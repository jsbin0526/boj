n, r, c = map(int, input().split())

def Z(n, r, c, result):
    if n == 1:
        return r * 2 + c + result
    
    half = 2 ** (n-1)
    
    if r >= half and c >= half: #4사분면
        return Z(n-1, r-half, c-half, result + half * half * 3)
    elif r >= half > c: #3사분면
        return Z(n-1, r-half, c, result + half * half * 2)
    elif c >= half > r: #2사분면
        return Z(n-1, r, c-half, result + half * half)
    else: #1사분면
        return Z(n-1, r, c, result)


print(Z(n, r, c, 0))