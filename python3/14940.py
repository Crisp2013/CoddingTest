import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

maps = [[]]*n
output = [[-1 for i in range(m)] for j in range(n)]


worklist=[]
visited = set()
for i in range(n):
    maps[i]=list(map(int, input().split()))
    for j in range(m):
        if maps[i][j]==2:
            worklist.append((j,i,0))
        if maps[i][j]==0:
            output[i][j] = 0
            


while len(worklist)!=0:
    (x,y,day)=worklist.pop(0)
    if (x,y) in visited:
        continue
    visited.add((x,y))
    output[y][x]=day

    if x>0 and (x-1,y) not in visited and maps[y][x-1]!=0:
        worklist.append((x-1,y,day+1))
    if y>0 and (x,y-1) not in visited and maps[y-1][x]!=0:
        worklist.append((x,y-1,day+1))


    if x<m-1 and (x+1,y) not in visited and maps[y][x+1]!=0:
        worklist.append((x+1,y,day+1))
    if y<n-1 and (x,y+1) not in visited and maps[y+1][x]!=0:
        worklist.append((x,y+1,day+1))

for i in range(n):
    print(str(output[i]).replace("[","").replace("]","").replace(",",""))
