from collections import deque
import copy
n, m = list(map(int, input().split()))

maps = [[]]*n
virus = []
for i in range(n):
    maps[i]=list(map(int, input().split()))
    for j in range(m):
        if maps[i][j]==2:
            virus.append((i,j))

maxval = 0
def calc_size(a1,a2,a3):
    global virus
    global maps
    global maxval
    work_list = deque(virus.copy())
    map_test = copy.deepcopy(maps)
    map_test[a1//m][a1%m]=1
    map_test[a2//m][a2%m]=1
    map_test[a3//m][a3%m]=1
    # print("b")
    # for i in range(n):
    #     print(map_test[i])
    while len(work_list)!=0:
        (x,y)=work_list.pop()

        if x>0 and map_test[x-1][y]==0:
            map_test[x-1][y]=2
            work_list.append((x-1,y))

        if x<n-1 and map_test[x+1][y]==0:
            map_test[x+1][y]=2
            work_list.append((x+1,y))

        if y>0 and map_test[x][y-1]==0:
            map_test[x][y-1]=2
            work_list.append((x,y-1))

        if y<m-1 and map_test[x][y+1]==0:
            map_test[x][y+1]=2
            work_list.append((x,y+1))


    survive_cell=0
    for i in range(n):
        for j in range(m):
            if map_test[i][j]==0:
                survive_cell+=1
    # if maxval<survive_cell:
    #     print("a")
    #     for i in range(n):
    #         print(map_test[i])
    return survive_cell

for a1 in range(0,n*m):
    for a2 in range(a1+1,n*m):     
        for a3 in range(a2+1,n*m):   
            if maps[a1//m][a1%m] != 0:
                continue   
            if maps[a2//m][a2%m] != 0:
                continue   
            if maps[a3//m][a3%m] != 0:
                continue
            maxval=max(maxval,calc_size(a1,a2,a3))

print(maxval)