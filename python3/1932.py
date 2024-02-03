n = int(input())
maps = [[]]*n

for i in range(n):
    maps[i] = list(map(int, input().split()))
    
    
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            maps[i][j] = maps[i][j]+maps[i-1][j]
        elif j == i:
            maps[i][j] = maps[i][j]+maps[i-1][j-1]
            
        else:
            maps[i][j] = maps[i][j]+max(maps[i-1][j-1], maps[i-1][j])
print(max(maps[n-1]))
            
    
    