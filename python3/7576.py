import sys
from collections import deque
input = sys.stdin.readline

m, n = list(map(int, input().split()))

maps = [[]] * n
work_list = deque()

notdone_list = set([])

for i in range(n):
    maps[i] = list(map(int, input().split()))
    for j in range(m):
        if maps[i][j]==1:
            work_list.append((0, i, j))
        if maps[i][j]!=-1:
            notdone_list.add((i, j))
    
day_max = -1
while len(work_list)!=0:
    days, x, y = work_list.popleft()
    notdone_list.remove((x, y))
    # print(maps)
    if x>0 and maps[x-1][y] == 0:
        maps[x-1][y] = 1 
        work_list.append((days+1, x-1, y))
    if y>0 and maps[x][y-1] == 0:
        maps[x][y-1] = 1 
        work_list.append((days+1, x, y-1))
    if x<n-1 and maps[x+1][y] == 0:
        maps[x+1][y] = 1 
        work_list.append((days+1, x+1, y))
    if y<m-1 and maps[x][y+1] == 0:
        maps[x][y+1] = 1 
        work_list.append((days+1, x, y+1))
    day_max = max(day_max, days)

if len(notdone_list)>0:
    print(-1)
else:
    print(day_max)