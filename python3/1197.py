'''
Kruskal MST 문제
'''

import sys
input = sys.stdin.readline

v, e = list(map(int, input().split()))

edges = []

for i in range(e):
    edges.append(tuple(map(int,input().split())))

edges = sorted(edges, key=lambda x:x[2])

answer = 0

mst = [-1]*(v+1)
temp = edges.pop(0)
mst[temp[0]]=temp[0]
mst[temp[1]]=temp[0]
answer+=temp[2]
# print(temp)

for i in range(v-1 -1):
    # print(mst)
    temp = edges.pop(0)
    while (mst[temp[0]]==mst[temp[1]])\
        and not (mst[temp[0]]==-1 and mst[temp[1]]==-1):
        #두 값이 서로 같으면 사이클임!
        #단 둘다 -1일때는 제외!
        temp = edges.pop(0)
    # print(temp)
    if mst[temp[0]]==-1 and mst[temp[1]]==-1:
        mst[temp[0]]=temp[0]
        mst[temp[1]]=temp[0]
        answer+=temp[2]
    elif mst[temp[1]]==-1:
        mst[temp[1]]=mst[temp[0]]
        answer+=temp[2]
    elif mst[temp[0]]==-1:
        mst[temp[0]]=mst[temp[1]]
        answer+=temp[2]
    else: #둘이 서로 다른 구역일때
        from_val = mst[temp[0]]
        to_val = mst[temp[1]]
        for i in range(len(mst)):
            if mst[i]==from_val:
                mst[i]=to_val#어느 한쪽의 영역을 흡수?하는 과정
        answer+=temp[2]
# print(mst)
print(answer)