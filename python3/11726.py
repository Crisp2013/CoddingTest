n = int(input())

lists = [0] * (n+1)


lists[1] = 1
if n == 1:
    print(1)
    exit()

lists[2] = 2

for i in range(3,n+1):
    lists[i]=lists[i-1]+lists[i-2]
    
print(lists[n]%10007)