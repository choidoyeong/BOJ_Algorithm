from sys import stdin
roof = int(stdin.readline())
for i in range(0, roof):
	num = int(stdin.readline())
	dp = [1]
	for n in range(1, num+1):
		dp.append(0)	
		if n-1 >= 0: dp[n] += dp[n-1]
		if n-2 >= 0: dp[n] += dp[n-2]
		if n-3 >= 0: dp[n] += dp[n-3]
	print(dp[num])
