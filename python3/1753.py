import sys
input = sys.stdin.readline
import heapq
n, e= list(map(int, input().split()))

start = int(input())

edges = dict()

for i in range(1,n+1):
    edges[i]=[]

for i in range(e):
    (u,v,w)= list(map(int, input().split()))
    edges[u].append((v,w))

INF = int(10e9)
visited = [False]*(n+1)
distance = [INF]*(n+1)
distance_heapq = []

for i in range(1,n+1):
    heapq.heappush(distance_heapq, (INF, i))

distance[start]=0
heapq.heappush(distance_heapq, (0, start))

for i in range(n):
    cur = heapq.heappop(distance_heapq)[1]
    while visited[cur]:
        cur = heapq.heappop(distance_heapq)[1]
    
    for next_node in edges[cur]:
        if distance[next_node[0]] > distance[cur] + next_node[1]:
            distance[next_node[0]] = distance[cur] + next_node[1]
            heapq.heappush(distance_heapq, (distance[next_node[0]], next_node[0]))
    visited[cur]=True
for i in range(1,n+1):
    if distance[i]>=INF:
        print("INF")
    else:
        print(distance[i])