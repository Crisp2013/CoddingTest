n = int(input())%1000000007

dp = [0]*4

dp[1]=1

for i in range(2,n+1):
    dp[i%3]=(dp[(i-1)%3]+dp[(i-2)%3])%1000000007
print(dp[n%3])

