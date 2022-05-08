a, b, c = [int(input()) for _ in range(3)]
if a + b + c == 180:
    if a == b or b == c or a == c:
        if a == b == c:
            print("Equilateral")
        else:
            print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")