n = int(input())

lists = []


for i in range(n):
    lists.append(tuple(map(int, input().split())))

house_r = [lists[0][0]]
house_g = [lists[0][1]]
house_b = [lists[0][2]]

house_n = 1
while True:
    house_r.append(min(house_g[house_n-1],house_b[house_n-1])+lists[house_n][0])
    house_g.append(min(house_r[house_n-1],house_b[house_n-1])+lists[house_n][1])
    house_b.append(min(house_r[house_n-1],house_g[house_n-1])+lists[house_n][2])
    if house_n == n-1:
        break
    house_n = house_n + 1 
print(min(house_r[-1],house_g[-1],house_b[-1]))
    # print(min(min(house_r[2**(n-1):]),min(house_g[2**(n-1):]),min(house_n[2**(n-1):])))















