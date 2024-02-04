import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))

gp = dict()
gp_set = set()
dot_set = set()
for i in range(1,n+1):
    gp[i]=[]
    dot_set.add(i)

for i in range(m):
    u, v = list(map(int, input().split()))
    gp[u].append(v)
    gp[v].append(u)
    gp_set.add((u,v))

work_list=deque()

answer = 0
while len(gp_set) > 0:

    work_list.append(gp_set.pop())
    answer = answer + 1
    while len(work_list) != 0:
        u,v=work_list.popleft()
        dot_set.discard(u)
        dot_set.discard(v)

        for i in gp[u]:
            if (u,i) in gp_set:
                work_list.append((u,i))
                gp_set.remove((u,i))
            if (i,u) in gp_set:
                work_list.append((i,u))
                gp_set.remove((i,u))
        
        for i in gp[v]:
            if (v,i) in gp_set:
                work_list.append((v,i))
                gp_set.remove((v,i))
            if (i,v) in gp_set:
                work_list.append((i,v))
                gp_set.remove((i,v))
                        
print(answer+len(dot_set))
                