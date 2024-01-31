n = int(input())

price=list(map(int, input().split()))


dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i]=price[i-1]
    for j in range(1,i):
        dp[i]=min(price[j-1]+dp[i-j], dp[i])
        
print(dp[n])
        
