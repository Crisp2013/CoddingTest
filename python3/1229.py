n = int(input())

dp = [10e9]*(n+1)
sets = []
i = 1
j = 1
while i<=n:
    # print(i)
    dp[i]=1
    sets.append(i)
    i+=(4*j+1)
    j+=1

for i in range(1,n+1):
    if dp[i]!=-1:
        for j in sets:
            if j>i: break
            dp[i]=min(dp[i],dp[i-j]+1)
print(dp[n])

        
