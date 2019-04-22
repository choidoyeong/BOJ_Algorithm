from sys import stdin
dp = [0] * 1000001
num = int(stdin.readline())
for n in range(2,num+1):
    if n % 3 == 0:
        dp[n] = dp[n//3]+1 if (dp[n] == 0 or dp[n] > dp[n//3]+1) else dp[n]
    if n % 2 == 0:
        dp[n] = dp[n//2]+1 if (dp[n] == 0 or dp[n] > dp[n//2]+1) else dp[n]
    if n-1 > 0:
        dp[n] = dp[n-1]+1 if (dp[n] == 0 or dp[n] > dp[n-1]+1) else dp[n]
print(dp[num])