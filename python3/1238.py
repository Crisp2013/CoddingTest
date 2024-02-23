#다익스트라알고리즘 연습
#TODO: 그래프를 뒤집어서 2번 다익스트라로 줄일것
INF = int(1e9)
import sys
import heapq
input = sys.stdin.readline
n, m, x = list(map(int, input().split()))

graph = dict()
for i in range(1,n+1):
    graph[i]=[]

for i in range(1,m+1):
    temp = list(map(int, input().split()))
    graph[temp[0]].append((temp[1],temp[2]))
distance = [INF]*(n+1)
visited = [False]*(n+1)

#5000개 이하에서는 우선순위 큐를 이용하지 않고 처리 가능
def get_smallest_node():
    global distance
    global visited
    min=INF
    idx = 0 #거리가 가장 짧은 노드
    for i in range(1,n+1):
        if visited[i]!=True:
            if distance[i]<min:
                min=distance[i]
                idx=i
    return idx

#print(graph)
#TODO:I->X->I의 최대값을 구해야함

each_distance = [INF]*(n+1)
for start in range(1,n+1):
    distance = [INF]*(n+1)
    distance_heap = []
    for i in range(1,n+1):
        heapq.heappush(distance_heap,(INF,i))
    visited = [False]*(n+1)

    distance[start]=0
    heapq.heappush(distance_heap,(0,start))
    
    current = start
    
    #중요:반복 횟수는 무조건 n회가 된다(결국 모든 정점을 방문해야함)
    for i in range(n):
        if i!=0:#처음이 아니면
            while True:
                dis, current = heapq.heappop(distance_heap)
                if visited[current]!=True:
                    break
        visited[current]=True
        for edge in graph[current]:
            distance[edge[0]]=min(distance[edge[0]],distance[current]+edge[1])
            heapq.heappush(distance_heap,(distance[edge[0]],edge[0]))#작은값으로 갱식

    each_distance[start] = distance[x]
    
distance = [INF]*(n+1)
distance_heap = []
for i in range(1,n+1):
    heapq.heappush(distance_heap,(INF,i))
visited = [False]*(n+1)

distance[x]=0
heapq.heappush(distance_heap,(0,start))
    
current = x
    
#중요:반복 횟수는 무조건 n회가 된다(결국 모든 정점을 방문해야함)
for i in range(n):
    if i!=0:#처음이 아니면
        while True:
            dis, current = heapq.heappop(distance_heap)
            if visited[current]!=True:
                break
    visited[current]=True
    for edge in graph[current]:
        distance[edge[0]]=min(distance[edge[0]],distance[current]+edge[1])
        heapq.heappush(distance_heap,(distance[edge[0]],edge[0]))#작은값으로 갱식

for i in range(n+1):
    each_distance[i] = each_distance[i] + distance[i]
each_distance.pop(0)
print(max(each_distance))

    


