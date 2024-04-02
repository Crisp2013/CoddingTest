'''
    문제 틀림:
    힌트 - 정방향이 아니라 역방향으로 풀어야 한다
    역방향으로 해서 끝점에서 max값을 구하면 됨
'''

from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    n, k = list(map(int, input().split()))
    d = list(map(int, input().split()))
    d = [-1]+d #1부터 시작하도록
    
    gp = dict()
    for i in range(1,n+1):
        gp[i]={
            "buildrequire":0,
            "starttime":0,
            "nextnode":[]
        }

    for i in range(k):
        x,y= list(map(int, input().split()))
        gp[x]["nextnode"].append(y)
        gp[y]["buildrequire"]+=1
    
    w = int(input())
    

    work_node=deque()
    for i in range(1,n+1):
        if gp[i]["buildrequire"] == 0:
            work_node.append((i,0)) #현재노드, 걸린 시간

    while len(work_node)!=0:
        current = work_node.pop()#DFS로 구현
        current_node = current[0]
        current_time = current[1]
        if gp[current_node]["buildrequire"] != 0:
            continue
        for next_node in gp[current_node]["nextnode"]:
            gp[next_node]["buildrequire"]-=1
            gp[next_node]["starttime"]=max(gp[next_node]["starttime"],current_time+d[current_node])
            work_node.append((next_node,current_time+d[current_node]))
    print(gp[w]["starttime"]+d[w])


    