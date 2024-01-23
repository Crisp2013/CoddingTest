import sys
input= sys.stdin.readline

(n,m,v) = list(map(int, input().split()))

graph = {}
# n

#이런식으로 리스트를 만들면 시간복잡도는 O(n)
#인접행렬(완전2차원) 이용시 시간복잡도 O(n^2)
for i in range(n):
    graph[i+1] = []
# m
for i in range(m):
    (a,b) = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i+1].sort(reverse=True) #스택 순서때문
    
#DFS
#스택 이용
task_list = [v]
visited = []
while True:
    current_point = task_list.pop(-1)
    if current_point not in visited:
        visited.append(current_point)
    for i in graph[current_point]:
        if i not in visited:
            task_list.append(i)
    if len(task_list) == 0:
        break;
print(str(visited).replace("[","").replace(", "," ").replace("]",""))


for i in range(n):
    graph[i+1].sort()

#BFS
#큐이용
task_list = [v]
visited = []
while True:
    current_point = task_list.pop(0)
    if current_point not in visited:
        visited.append(current_point)
    for i in graph[current_point]:
        if i not in visited:
            task_list.append(i)
    if len(task_list) == 0:
        break;
print(str(visited).replace("[","").replace(", "," ").replace("]",""))