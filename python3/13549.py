n, k = list(map(int, input().split()))

maps = [-1]*100001
maps[n]=0
work_list = [n]
while len(work_list)>0:
    # print(work_list)
    cur = work_list.pop(0)
    # print(cur)
    # print(cur)
    if cur == k:
        print(maps[k])
        exit()
    temp = cur
    while temp<=100000:
        if maps[temp]<maps[cur]:
            maps[temp]=maps[cur]
        if temp == k:
            print(maps[cur])
            exit()
        # if cur+1 == k or cur-1 == k:
        #     print(maps[cur]+1)
        #     exit()
        if temp < 100000 and maps[temp+1]==-1:
            work_list.append(temp+1)
            maps[temp+1]=maps[cur]+1
        if temp > 0 and maps[temp-1]==-1:
            work_list.append(temp-1)
            maps[temp-1]=maps[cur]+1
        if temp == 0:
            break
        if temp >= k*2:
            break
        temp = temp*2