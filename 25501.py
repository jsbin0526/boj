def recursion(s, l, r):
    global COUNT
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        COUNT += 1
        return recursion(s, l+1, r-1)

def isPalindrom(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    COUNT = 0
    print(isPalindrom(input()), COUNT+1)