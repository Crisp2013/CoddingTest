#다익스트라 연습2
#heapq사용연습좀
#개념자체는 익힌거 같은데
INF = int(10e9)
import sys
input = sys.stdin.readline
import heapq
n, e = list(map(int, input().split()))

edges = dict()
for i in range(1,n+1):
    edges[i]=[]
for i in range(e):
    temp = list(map(int, input().split()))
    edges[temp[0]].append((temp[1],temp[2]))#temp2:distance
    edges[temp[1]].append((temp[0],temp[2]))

v1, v2= list(map(int, input().split()))

distance_v1=[INF]*(n+1)
distance_v2=[INF]*(n+1)

distance_heapq = []
visited = [False]*(n+1)
for i in range(1,n+1):
    heapq.heappush(distance_heapq,(INF,i))

distance_v1[v1]=0
heapq.heappush(distance_heapq,(0,v1))

for i in range(n):
    current = heapq.heappop(distance_heapq)[1]
    while visited[current]==True:
        current = heapq.heappop(distance_heapq)[1]
    # print(current)
    for next_n in edges[current]:
        # print(next_n[0],next_n[1])
        # print(current,"->",next_n[0],":",distance_v1[next_n[0]],distance_v1[current]+next_n[1])
        if distance_v1[next_n[0]]>distance_v1[current]+next_n[1]:
            distance_v1[next_n[0]]=distance_v1[current]+next_n[1]
            heapq.heappush(distance_heapq,(distance_v1[next_n[0]],next_n[0]))
    visited[current]=True

    
distance_heapq = []
visited = [False]*(n+1)
for i in range(1,n+1):
    heapq.heappush(distance_heapq,(INF,i))

distance_v2[v2]=0
heapq.heappush(distance_heapq,(0,v2))

for i in range(n):
    current = heapq.heappop(distance_heapq)[1]
    while visited[current]==True:
        current = heapq.heappop(distance_heapq)[1]
    # print(current)
    for next_n in edges[current]:
        # print(next_n[0],next_n[1])
        # print(current,"->",next_n[0],":",distance_v2[next_n[0]],distance_v2[current]+next_n[1])
        if distance_v2[next_n[0]]>distance_v2[current]+next_n[1]:
            distance_v2[next_n[0]]=distance_v2[current]+next_n[1]
            heapq.heappush(distance_heapq,(distance_v2[next_n[0]],next_n[0]))
    visited[current]=True
# print(distance_v1)
# print(distance_v2)
if distance_v2[1]>=INF:
    print(-1)
elif distance_v1[1]>=INF and distance_v2[1]>=INF:
    print(-1)
elif distance_v1[n]>=INF and distance_v2[n]>=INF:
    print(-1)
else:
    print(min(distance_v1[1]+distance_v2[n]+distance_v2[v1],distance_v2[1]+distance_v1[n]+distance_v2[v1]))
