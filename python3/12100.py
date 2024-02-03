n = int(input())


maps = [[]]*n
max_val = 0
for i in range(n):
    maps[i] = list(map(int, input().split()))
    max_val = max(max(maps[i]), max_val)

work_list = [(maps,0)]

# maps[i][j]
#   -> j
# |
# V
# i

while len(work_list)!=0:
    temp = work_list.pop(-1)
    depth = temp[1]
    maps_cur = temp[0]
    
    cur_max_val = 0
    for i in range(n):
        cur_max_val = max(max(maps_cur[i]), cur_max_val)
    if False:
        for i in range(n):
            print(maps_cur[i])
        print(cur_max_val, depth)    
    if cur_max_val*(2**(5-depth)) < max_val:
        continue
    if cur_max_val>max_val:
        max_val=cur_max_val
        
    if depth >= 5:
        continue
        
    
    
    #위로 올리기
    maps_next=[arr[:] for arr in maps_cur]
    movedset = set()
    for i in range(n):#세로
        for j in range(n):#가로
            for k in range(i-1,-2,-1):
                if k == -1:
                    maps_next[i][j],maps_next[0][j]=0,maps_next[i][j]
                    break
                if maps_next[k][j]!=0:
                    if maps_next[k][j] == maps_next[i][j]:
                        if (k,j) not in movedset:
                            movedset.add((k,j))
                            maps_next[i][j],maps_next[k][j]=0,maps_next[i][j]*2
                        else:   
                            maps_next[i][j],maps_next[k+1][j]=0,maps_next[i][j]
                            
                        break
                    else:
                        maps_next[i][j],maps_next[k+1][j]=0,maps_next[i][j]
                        break
    work_list.append((maps_next,depth+1))


    #아래로로 내리기
    maps_next=[arr[:] for arr in maps_cur]
    movedset = set()
    for i in range(n-1,-1,-1):#세로
        for j in range(n):#가로
            for k in range(i+1,n+1):
                if k == n:
                    maps_next[i][j],maps_next[n-1][j]=0,maps_next[i][j]
                    break
                if maps_next[k][j]!=0:
                    if maps_next[k][j] == maps_next[i][j]:
                        if (k,j) not in movedset:
                            movedset.add((k,j))
                            maps_next[i][j],maps_next[k][j]=0,maps_next[i][j]*2
                        else:
                            maps_next[i][j],maps_next[k-1][j]=0,maps_next[i][j]
                        break
                    else:
                        maps_next[i][j],maps_next[k-1][j]=0,maps_next[i][j]
                        break
    work_list.append((maps_next,depth+1))

    #왼쪽으로
    maps_next=[arr[:] for arr in maps_cur]
    movedset = set()
    for j in range(n):#가로
        for i in range(n):#세로
            for k in range(j-1,-2,-1):
                if k == -1:
                    maps_next[i][j],maps_next[i][0]=0,maps_next[i][j]
                    break
                if maps_next[i][k]!=0:
                    if maps_next[i][k] == maps_next[i][j]:
                        if (i,k) not in movedset:
                            movedset.add((i,k))
                            maps_next[i][j],maps_next[i][k]=0,maps_next[i][j]*2
                        else:
                            maps_next[i][j],maps_next[i][k+1]=0,maps_next[i][j]
                        break
                    else:
                        maps_next[i][j],maps_next[i][k+1]=0,maps_next[i][j]
                        break
    work_list.append((maps_next,depth+1))

    #오른쪽로로 내리기
    maps_next=[arr[:] for arr in maps_cur]
    movedset = set()
    for j in range(n-1,-1,-1):#가로
        for i in range(n):#세로
            for k in range(j+1,n+1):
                if k == n:
                    maps_next[i][j],maps_next[i][n-1]=0,maps_next[i][j]
                    break
                if maps_next[i][k]!=0:
                    if maps_next[i][k] == maps_next[i][j]:
                        if (i,k) not in movedset:
                            movedset.add((i,k))
                            maps_next[i][j],maps_next[i][k]=0,maps_next[i][j]*2
                        else:
                            maps_next[i][j],maps_next[i][k-1]=0,maps_next[i][j]
                        break
                    else:
                        maps_next[i][j],maps_next[i][k-1]=0,maps_next[i][j]
                        break    
    work_list.append((maps_next,depth+1))

    # for i in range(n):
    #     print(maps_next[i])
    # print()
print(max_val)
        