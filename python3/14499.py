n, m, x, y, k = list(map(int, input().split()))

maps = [[]]*n
for i in range(n):
    maps[i]=list(map(int, input().split()))
    
works =list(map(int, input().split()))


BOTTOM=0
EAST=1
WEST=2
NORTH=3
SOUTH=4
TOP=5

dices = [0,0,0,0,0,0]


for i in works:
    if i==EAST:
        y = y + 1
        if y == m:
            y = y -1
            continue
        dices[BOTTOM],dices[EAST],dices[TOP],dices[WEST]=dices[EAST],dices[TOP],dices[WEST],dices[BOTTOM]
        if maps[x][y]==0:
            maps[x][y]=dices[BOTTOM]
        else:
            dices[BOTTOM]=maps[x][y]
            maps[x][y]=0
    if i==WEST:
        y = y - 1
        if y == -1:
            y = y + 1
            continue
        dices[BOTTOM],dices[WEST],dices[TOP],dices[EAST]=dices[WEST],dices[TOP],dices[EAST],dices[BOTTOM]
        if maps[x][y]==0:
            maps[x][y]=dices[BOTTOM]
        else:
            dices[BOTTOM]=maps[x][y]
            maps[x][y]=0
    if i==NORTH:
        x = x - 1
        if x == -1:
            x = x + 1
            continue
        dices[BOTTOM],dices[NORTH],dices[TOP],dices[SOUTH]=dices[NORTH],dices[TOP],dices[SOUTH],dices[BOTTOM]
        if maps[x][y]==0:
            maps[x][y]=dices[BOTTOM]
        else:
            dices[BOTTOM]=maps[x][y]
            maps[x][y]=0
    if i==SOUTH:
        x = x + 1
        if x == n:
            x = x - 1
            continue
        dices[BOTTOM],dices[SOUTH],dices[TOP],dices[NORTH]=dices[SOUTH],dices[TOP],dices[NORTH],dices[BOTTOM]
        if maps[x][y]==0:
            maps[x][y]=dices[BOTTOM]
        else:
            dices[BOTTOM]=maps[x][y]
            maps[x][y]=0
    print(dices[TOP])
    
    
    
    
    
