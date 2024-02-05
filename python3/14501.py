n = int(input())

maps = [[]]*(n+1)
dp=[0]*(n+2)
for i in range(1, n+1):
    maps[i] = list(map(int, input().split()))
    
for i in range(1, n+2):
    dp[i]=dp[i-1]
    for j in range(1,i):
        if j+maps[j][0] == i:
            
            dp[i]=max(dp[i], dp[j] + maps[j][1])
    # print(dp[i])
print(dp[n+1])
    
    