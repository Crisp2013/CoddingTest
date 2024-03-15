n, m = list(map(int, input().split()))

DIRECTION_N = 0
DIRECTION_E = 1
DIRECTION_S = 2
DIRECTION_W = 3




r, c, d = list(map(int, input().split()))

maps = [[]]*n
for i in range(n):
    maps[i] = list(map(int, input().split()))

answer = 0
while True:
    # print(r,c,d,":",answer)
    dirction = [0,0,0,0]
    dirction[DIRECTION_N] = maps[r-1][c] if r>0 else 1
    dirction[DIRECTION_S] = maps[r+1][c] if r<n-1 else 1
    dirction[DIRECTION_W] = maps[r][c-1] if c>0 else 1
    dirction[DIRECTION_E] = maps[r][c+1] if c<m-1 else 1
    if maps[r][c]==0:
        maps[r][c]=2
        answer+=1
    elif dirction[0]==0 or dirction[1]==0 or dirction[2]==0 or dirction[3]==0:
        d=(d-1)%4
        if dirction[d]==0:
            if d == DIRECTION_N:
                r-=1
            elif d == DIRECTION_S:
                r+=1
            elif d == DIRECTION_W:
                c-=1
            elif d == DIRECTION_E:
                c+=1
    elif dirction[0]!=0 and dirction[1]!=0 and dirction[2]!=0 and dirction[3]!=0:
        if dirction[(d-2)%4]==1:
            break
        else:
            if d == DIRECTION_N:
                r+=1
            elif d == DIRECTION_S:
                r-=1
            elif d == DIRECTION_W:
                c+=1
            elif d == DIRECTION_E:
                c-=1
    else:
        print("error")
        break
print(answer)