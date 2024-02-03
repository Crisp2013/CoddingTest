n = int(input())

maps = [0]*n

for i in range(n):
    maps[i]=int(input())

maps.sort()
for i in range(n):
    print(maps[i])