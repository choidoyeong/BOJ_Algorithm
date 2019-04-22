from sys import stdin
num = int(stdin.readline())
dp = [0, 1, 3]
if num > 2:
    for n in range(3, num+1):
        dp.append(dp[n-1]+dp[n-2]+dp[n-2])
print(dp[num]%10007)