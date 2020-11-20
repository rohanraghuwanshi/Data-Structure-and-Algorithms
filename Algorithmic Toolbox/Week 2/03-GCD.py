def gcd(a, b):
	if a==0:
		return b
	elif  b == 0:
		return a
	else:
		return	gcd(b%a,a)

a, b = map(int, input().split())
print(gcd(a, b))