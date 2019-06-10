from sys import stdin
num = stdin.readline().split()
for n in range(0, len(num)):
	num[n] = int(num[n])
def gcd(a, b):
	if a % b == 0: 
		return b
	return gcd(b, a % b)
r = gcd(num[0], num[1])
print(str(r)+ '\n' + str(num[0]*num[1]//r))
