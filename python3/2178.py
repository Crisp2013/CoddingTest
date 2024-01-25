import sys
input = sys.stdin.readline

n, m = list(map(int,input().split()))

maps = [[]] * n

for i in range(n):
    maps[i]= list(map(int, list(str(input().rstrip()))))

    
work_list = [(0,0)]

while True:


    
    coord = work_list.pop(0)#0번째 원소를 꺼내야 queue
    x, y = list(coord)
    
    if x == n-1 and y == m-1:
        # for i in range(n):
        #     print(maps[i])
        print(maps[x][y])
        break
    
    if x > 0 and maps[x-1][y] == 1:
        work_list.append((x-1, y))
        maps[x-1][y] = maps[x][y] + 1
    
    if y > 0 and maps[x][y-1] == 1:
        work_list.append((x, y-1))
        maps[x][y-1] = maps[x][y] + 1
    
    if x < n-1 and maps[x+1][y] == 1:
        work_list.append((x+1, y))
        maps[x+1][y] = maps[x][y] + 1
        
    if y < m-1 and maps[x][y+1] == 1:
        work_list.append((x, y+1))
        maps[x][y+1] = maps[x][y] + 1
    
