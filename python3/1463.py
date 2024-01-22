x = int(input())

if x == 1:
    print(0)
    exit()
    
dp=[10000001] * (10**6+1)
dp[1]=0
for i in range(1,x):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    if i<=500000:
        dp[i*2] = min(dp[i*2], dp[i]+1)
    if i<=333333:
        dp[i*3] = min(dp[i*3], dp[i]+1)
    


print(dp[x])

    
# indexed = set([])

# current = set([x])
# new_set = set([])
# k = 0
# while True:
#     for i in current:
#         if i <= 3:
#             print(k+1)
#             exit()
#         if i % 3 == 0:
#             new_set.add(i//3)
#         if i % 2 == 0:
#             new_set.add(i//2)
#         new_set.add(i-1)
        
#     current = new_set - indexed
#     indexed = new_set | indexed
           
            
#     k=k+1