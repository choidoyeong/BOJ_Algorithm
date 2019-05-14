from sys import stdin
num = int(stdin.readline())
dp = [0,2,7, 22]
dp2 = [0, 0, 0, 1]
if num >= 4:
	for n in range(4, num+1):
		dp2.append((dp2[n-1]+dp[n-3])%1000000007)
		dp.append((dp[n-1]*2 + dp[n-2]*3 + dp2[n]*2)%1000000007)
print(dp[num])
