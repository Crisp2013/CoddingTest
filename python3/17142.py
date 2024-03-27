
def maptest():
    worklist = []
    while True:
        

n, m = list(map(int, input().split()))

map = [[]]*n
virus = []
for i in range(n):
    map[i] = list(map(int, input().split()))
    for j in range(n):
        if map[i][j] == 2:
            virus.append((i,j))