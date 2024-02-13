n = int(input())
a = list(map(int, input().split()))

temp = []
points = -1

for i in range(n):
    # print(temp,points)
    if points == -1:
        temp.append(a[i])
        points = points + 1
        continue
    if temp[points]<a[i]:
        temp.append(a[i])
        points = points + 1
        continue
    if temp[0]<a[i]:
        temp[0]=a[i]
        points = 0
        continue

    for j in range(points-1,-1,-1):
        if temp[j]>a[i]:
            temp[j+1]=a[i]
            points = j + 1
            break

print(points+1)
print(str(temp).replace(',','').replace(']','').replace('[',''))