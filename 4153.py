while True:
	a, b, c = sorted(map(int, input().split()))
	if not(a and b and c): break
	elif c**2 == a**2 + b**2: print("right")
	else: print("wrong")