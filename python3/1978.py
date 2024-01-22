n = int(input())

nums=list(map(int,input().split()))

a=len(nums)
for i in range(n):
    if nums[i]==1:
        a=a-1
        continue
    for j in range(2,nums[i]):
        if nums[i]%j==0:
            a=a-1
            break
print(a)    
        