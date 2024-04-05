'''
    모르겠어...
'''

n, k = list(map(int, input().split()))

jewel_info = []
max_size = 0
for i in range(n):
    #[size][value]
    jewel_info.append(tuple(map(int, input().split())))
    max_size = max(max_size, jewel_info[-1][0])

bag_size = []
for i in range(k):
    bag_size.append(int(input()))

bag_size = sorted(bag_size)
jewel_info = sorted(jewel_info)

jewel_info_start_point = [-1]*(max_size+1)
for i in range(len(jewel_info)):
    jewel_info_start_point[jewel_info[i][0]] = i
temp = -1
for i in range(len(jewel_info_start_point)):
    if jewel_info_start_point[i]==-1:
        jewel_info_start_point[i]=temp
    else:
        temp=jewel_info_start_point[i]

print(jewel_info)
print(jewel_info_start_point)

for i in range(len(bag_size)):
    max_jewl=0
    max_val=0
    for j in range(jewel_info_start_point[i],-1,-1):
        if max_val<jewel_info[j][1]:


    