'''
    오답노트 - 정방향이 아니라 역방향으로 풀어야 한다
    역방향으로 해서 끝점에서 max값을 구하면 됨
    그럼 위상차수 필요없음
    그리고 BFS는 항상 옳다

    끝점을 저장해둘것(DP의 개념, 안그럼 느려짐)
'''

from collections import deque
import sys
input = sys.stdin.readline
#NOTE:3배 더 빠른 방법
# import io, os
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
T = int(input())

for t in range(T):
    n, k = list(map(int, input().split()))
    d = list(map(int, input().split()))
    d = [-1]+d #1부터 시작하도록
    
    gp = dict()

    for i in range(1,n+1):
        gp[i]=[]

    for i in range(k):
        x,y= list(map(int, input().split()))
        gp[y].append(x) #역방향
    
    w = int(input())

    endpoint_val = []

    work_node=deque()
    work_node.append(w) #현재노드, 걸린 시간
    time_test = [-1]*(n+1)
    time_test[w]=0
    while len(work_node)!=0:
        current_node = work_node.popleft()#BFS로 구현
        # print(time_test)
        for next_node in gp[current_node]:
            if time_test[next_node]<time_test[current_node]+d[current_node]:
                time_test[next_node]=time_test[current_node]+d[current_node]
                if next_node not in work_node:
                    work_node.append(next_node)
        if len(gp[current_node])==0:
            endpoint_val.append(time_test[current_node]+d[current_node])
    # print(endpoint_val)
    print(max(endpoint_val))


    