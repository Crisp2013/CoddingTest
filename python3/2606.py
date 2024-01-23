import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

computers = {}
for i in range(1,n+1):
    computers[i] = set()

m = int(input())
for i in range(m):
    u,v = list(map(int,input().split()))
    computers[u].add(v)
    computers[v].add(u)
    
work_list = deque([1])
visited = set()
while True:
    if len(work_list) == 0:
        break
    current=work_list.pop()
    visited.add(current)
    for i in computers[current]:
        if i not in visited:
            work_list.append(i)
print(len(visited)-1)
        
    