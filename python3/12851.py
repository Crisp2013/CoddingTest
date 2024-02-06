# from collections import deque
n, k = list(map(int, input().split()))

work_list = [(n,0)]
maps = [0]*1000001
min_val = 97283264287394
answer = 0

if n == k:
    print(0)
    print(1)
    exit()

while len(work_list) != 0:
    # print(work_list)
    temp_2 = work_list.pop(0)
    temp = temp_2[0]
    cur = temp_2[1]
    # print(temp,maps[temp])
    
    # if temp[0]<0:
    #     continue
    # if temp[0]>max(n,k)*2:
    #     continue
    
    if maps[temp] >= min_val:
        continue
        
    if temp>0:
        if temp - 1 == k:
            min_val = maps[temp] + 1
            answer = answer + 1
            continue
            
        if maps[temp-1] == cur + 1:
            work_list.append((temp-1,maps[temp]+1))
        if maps[temp-1] == 0:
            maps[temp-1]=maps[temp]+1
            work_list.append((temp-1,maps[temp]+1))
    
    if temp+1<1000001 and temp<k:    
        if temp + 1 == k:
            min_val = maps[temp] + 1
            answer = answer + 1
            continue
            
        if maps[temp+1] == cur + 1:
            work_list.append((temp+1,maps[temp]+1))
        if maps[temp+1] == 0:
            maps[temp+1]=maps[temp]+1
            work_list.append((temp+1,maps[temp]+1))
            
    if temp*2<1000001 and temp<k*2:     
        if temp * 2 == k:
            min_val = maps[temp] + 1
            answer = answer + 1
            continue
            
        if maps[temp*2] == cur+1:   
            work_list.append((temp*2,maps[temp]+1))
        if maps[temp*2] == 0:   
            maps[temp*2]=maps[temp]+1
            work_list.append((temp*2,maps[temp]+1))
print(min_val)
print(answer)