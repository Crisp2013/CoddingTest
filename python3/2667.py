import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

maps = [[]]*n

work_set = set()
work_list = deque()


for i in range(n):
    maps[i]=input().rstrip()
    for j in range(n):
        if maps[i][j]=='1':
            work_set.add((i,j))
result = []        
while len(work_set) !=0:
    temp = work_set.pop()
    work_list.append(temp)
    work_set.add(temp)
    part_size=0
    while len(work_list) !=0:
        temp = work_list.popleft()
        print(temp)
        x=temp[0]
        y=temp[1]
        if (x,y) in work_set:
            work_set.remove((x,y))    
            part_size = part_size+1
        else:
            continue
        if (x+1,y) in work_set:
            work_list.append((x+1,y))
        if (x,y+1) in work_set:
            work_list.append((x,y+1))
        if (x-1,y) in work_set:
            work_list.append((x-1,y))
        if (x,y-1) in work_set:
            work_list.append((x,y-1))
    result.append(part_size)
print(len(result))
print(str(sorted(result)).replace(",","").replace("]","").replace("[",""))
    