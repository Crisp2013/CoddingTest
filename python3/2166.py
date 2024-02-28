n = int(input())

coord_list = []
for i in range(n):
    temp = tuple(map(int, input().split()))
    coord_list.append(temp)

coord_first = coord_list.pop()

total_size = 0.0

for i in range(len(coord_list)-1):
    point1 = coord_first
    point2 = coord_list[i]
    point3 = coord_list[i+1]

    point_min = (min(point1[0],point2[0],point3[0]),min(point1[1],point2[1],point3[1]))
    point_max = (max(point1[0],point2[0],point3[0]),max(point1[1],point2[1],point3[1]))

    polybig = (point_max[0]-point_min[0])*(point_max[1]-point_min[1])
    poly1 = abs((point1[0]-point2[0])*(point1[1]-point2[1]))/2
    poly2 = abs((point2[0]-point3[0])*(point2[1]-point3[1]))/2
    poly3 = abs((point3[0]-point1[0])*(point3[1]-point1[1]))/2

    total_size = total_size + (polybig - poly1 - poly2 - poly3)
total_size = abs(total_size)
print(round(total_size,-1))