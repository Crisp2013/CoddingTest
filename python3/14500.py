from collections import deque
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

maps = [[]] * n

work_list = deque()
map_max = 0
for i in range(n):
    maps[i] = list(map(int, input().split()))
    map_max = max(max(maps[i]),map_max)
    for j in range(m):
        work_list.append((maps[i][j], 1, (i, j), (-1,-1), (-1,-1), (-1,-1)))

answer = 0
while len(work_list) != 0:
    temp = work_list.pop()
    block = [[]]*4
    # print(temp)
    sum_val = temp[0]
    block_num = temp[1]
    block[0] = temp[2]
    block[1] = temp[3]
    block[2] = temp[4]
    block[3] = temp[5]
    i,j = block[block_num-1]
    #조기종료 조건
    # if sum_val < answer - map_max * (4-block_num):
    #     continue
    if block_num == 4:
        answer = max(sum_val, answer)
        continue
    
    if i > 0 and (i-1, j) not in block:
        block[block_num] = (i-1, j)
        work_list.append((sum_val+maps[i-1][j], block_num+1, block[0], block[1], block[2], block[3]))
    if i < n-1 and (i+1, j) not in block:
        block[block_num] = (i+1, j)
        work_list.append((sum_val+maps[i+1][j], block_num+1, block[0], block[1], block[2], block[3]))
    if j > 0 and (i, j-1) not in block:
        block[block_num] = (i, j-1)
        work_list.append((sum_val+maps[i][j-1], block_num+1, block[0], block[1], block[2], block[3]))
    if j < m-1 and (i, j+1) not in block:
        block[block_num] = (i, j+1)
        work_list.append((sum_val+maps[i][j+1], block_num+1, block[0], block[1], block[2], block[3]))
        
    #T자 하드코딩
    if block[0][0] == block[1][0] == block[2][0]: #i값 동일?
        if i > 0 and (i-1, block[1][1]) not in block:
            block[block_num] = (i-1, block[1][1])
            work_list.append((sum_val+maps[i-1][block[1][1]], block_num+1, block[0], block[1], block[2], block[3]))
        if i < n-1 and (i+1, block[1][1]) not in block:
            block[block_num] = (i+1, block[1][1])
            work_list.append((sum_val+maps[i+1][block[1][1]], block_num+1, block[0], block[1], block[2], block[3]))
        
    if block[0][1] == block[1][1] == block[2][1]: #j값 동일?
        if j > 0 and (block[1][0], j-1) not in block:
            block[block_num] = (block[1][0], j-1)
            work_list.append((sum_val+maps[block[1][0]][j-1], block_num+1, block[0], block[1], block[2], block[3]))
        if j < m-1 and (block[1][0], j+1) not in block:
            block[block_num] = (block[1][0], j+1)
            work_list.append((sum_val+maps[block[1][0]][j+1], block_num+1, block[0], block[1], block[2], block[3]))
        
print(answer)