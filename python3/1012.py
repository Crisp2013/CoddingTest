import sys
input = sys.stdin.readline

t = int(input())
#set 안에는 tuple을 넣을것(list 못넣음)
#(1,2) : tuple
#{1,2} : set
#{1: 2}: dict
#[1, 2]: list

for i in range(t):
    (n, m, k) = list(map(int, input().split()))

    coord = set([])

    for j in range(k):
        coord.add(tuple(map(int, input().split())))

    worms = 0
    while len(coord)!=0:
        worms = worms + 1
        wl = [coord.pop()]

        while len(wl)!=0:
            temp = wl.pop()
            x, y = list(temp)
            
            # print(x, y, worms)
            
            if x > 0 and (x-1, y) in coord:
                wl.append((x-1, y))
                coord.remove((x-1, y))
            if y > 0 and (x, y-1) in coord:
                wl.append((x, y-1))
                coord.remove((x, y-1))
            if x < n-1 and (x+1, y) in coord:
                wl.append((x+1, y))
                coord.remove((x+1, y))
            if y < m-1 and (x, y+1) in coord:
                wl.append((x, y+1))
                coord.remove((x, y+1))
    print(worms)
