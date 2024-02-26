#visited 관리해서 메모리 초과/시간 초과 해결 필요
import sys
from collections import deque
input = sys.stdin.readline
n,m=list(map(int, input().split()))

map = [[]]*n

for i in range(n):
    map[i]=input()


work_list = deque([(0,0,1,True)])

while len(work_list)!=0:
    cur = work_list.popleft()
    # print(cur)
    x = cur[0]
    y = cur[1]
    if x==n-1 and y==m-1:
        print(cur[2])
        exit()
    
    if x!=0 and map[x-1][y]!='1':
        work_list.append((x-1,y,cur[2]+1,cur[3]))
    if x!=n-1 and map[x+1][y]!='1':
        work_list.append((x+1,y,cur[2]+1,cur[3]))
    if y!=0 and map[x][y-1]!='1':
        work_list.append((x,y-1,cur[2]+1,cur[3]))
    if y!=m-1 and map[x][y+1]!='1':
        work_list.append((x,y+1,cur[2]+1,cur[3]))

    if cur[3]:
        if x!=0 and map[x-1][y]=='1':
            work_list.append((x-1,y,cur[2]+1,False))
        if x!=n-1 and map[x+1][y]=='1':
            work_list.append((x+1,y,cur[2]+1,False))
        if y!=0 and map[x][y-1]=='1':
            work_list.append((x,y-1,cur[2]+1,False))
        if y!=m-1 and map[x][y+1]=='1':
            work_list.append((x,y+1,cur[2]+1,False))
print(-1)