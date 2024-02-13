n = int(input())

k=0

dp = [0]
for i in range(1,n+1):
    if (k+1)**2==i:
        dp.append(1)
        k = k+1
    else:
        temp = 9999999999
        for j in range(1,k+1):
            temp=min(temp,dp[i-j**2]+1)
        dp.append(temp)
# print(dp)
print(dp[n])

# O(n*sqrt(n))