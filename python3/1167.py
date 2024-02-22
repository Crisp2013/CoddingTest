#힌트: https://www.acmicpc.net/board/view/83695
n = int(input())
tree_list = dict()

for i in range(1,n+1):
    temp = list(map(int, input().split()))
    tree_list[temp[0]]=[]
    for j in range(len(temp)//2-1):
        tree_list[temp[0]].append((temp[j*2+1],temp[j*2+2]))
#print(tree_list)

max_val = 0
work_list = [(2,0)]

visited = [0]*(n+1)
start_point = 1
while len(work_list)!=0:
    coord_set = work_list.pop(-1)#DFS

    coord = coord_set[0]
    val = coord_set[1]
    
    max_val = max(max_val,val)
    if max_val == val:
        start_point = coord
    
    visited[coord]=1
    for next_coord in tree_list[coord]:
        if visited[next_coord[0]]!=1:
            work_list.append((next_coord[0],val+next_coord[1]))
    # visited[coord]=0#tree이므로 

work_list.append((start_point,0))
visited = [0]*(n+1)
while len(work_list)!=0:
    coord_set = work_list.pop(-1)#DFS

    coord = coord_set[0]
    val = coord_set[1]
    
    max_val = max(max_val,val)
    
    visited[coord]=1
    for next_coord in tree_list[coord]:
        if visited[next_coord[0]]!=1:
            work_list.append((next_coord[0],val+next_coord[1]))
    # visited[coord]=0 
            
print(max_val)



