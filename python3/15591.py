'''
    문제 틀림:
    힌트1 해당 문제는 트리이므로 그냥 거슬러 가면 됨(그래프 탐색방식 필요 없음)
    힌트2 USADO는 길이가 아니라, 엣지의 최소값
'''

import heapq

N, Q = list(map(int, input().split()))

INF = int(10e9)

USADO = dict()
for i in range(1,N+1):
    USADO[i]=[]
#지금보니 그래프가 아니라 트리네?
for i in range(N-1):
    p,q,r = list(map(int, input().split()))
    USADO[p].append((q,r))
    USADO[q].append((p,r))

def calc_distance(k,v):
    distance = [INF]*(N+1)
    distance[v]=0
    distance_que=[]
    visited = [False]*(N+1)

    for i in range(1,N+1):
        heapq.heappush(distance_que,(distance[i],i))#거리순 정렬

    for i in range(N):#N개의 정점만 확인 예정
        cur = heapq.heappop(distance_que)[1]
        while visited[cur]==True:
            cur = heapq.heappop(distance_que)[1]
        visited[cur]=True
        for next in USADO[cur]:
            distance[next[0]]=min(distance[next[0]],next[1])
            heapq.heappush(distance_que,(distance[next[0]],next[0]))#거리순 정렬
    distance.pop(0)
    sums = 0
    
    print(distance)
    for i in distance:
        if i>=k:
            sums+=1
    return sums

for i in range(Q):
    k,v = list(map(int, input().split()))
    print(calc_distance(k,v))