from sys import stdin
roop = int(stdin.readline())
def gcd(num1, num2):
	if num1 % num2 == 0:
		return num2
	return gcd(num2, num1 % num2)
for n in range(0, roop):
	num = stdin.readline().split()
	for i in range(0, len(num)):
		num[i] = int(num[i])
	s = 0
	for i in range(1, num[0]):
		for j in range(i+1, num[0]+1):
			s += gcd(num[i], num[j])
	print(s)
