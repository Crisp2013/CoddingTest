import sys
input = sys.stdin.readline
n = int(input())
task_list = [[]]*n
for i in range(n):
    task_list[i]=tuple(map(int, input().split()))

# print(task_list)

dp = [0]*(n+1)

dp_max = 0
for i in range(n):
    today = task_list[i]
    dp_max = max(dp[i],dp_max)
    if i+today[0]<=n:
        dp[i+today[0]]=max(dp_max+today[1],dp[i+today[0]])
print(max(dp))
    