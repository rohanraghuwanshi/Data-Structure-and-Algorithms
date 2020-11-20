def gcd(a, b):
	if a==0:
		return b
	elif  b == 0:
		return a
	else:
		return	gcd(b%a,a)

def lcm(a, b):
	#Since (LCM * GCD) = (a * b)
	return((a*b)//gcd(a, b))

a, b = map(int, input().split())
print(lcm(a, b))