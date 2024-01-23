import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))

lists = {}

for i in range(n):
    x,y=input().split()
    lists[x]=y
    

for i in range(m):
    x=input().split()[0]
    print(lists[x])
    
