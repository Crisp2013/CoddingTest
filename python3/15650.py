n, m = list(map(int, input().split()))


lists = []

lists_new = []
for i in range(1,n+1):
    lists.append([i])

lens = 1
while m!=lens:
    for a in lists:
        for i in range(max(a)+1,n+1):
            temp = a.copy()
            temp.append(i)
            lists_new.append(temp)

    lists=lists_new.copy()
    lists_new=[]
    lens = lens + 1
for a in lists:
    print(str(a).replace(",","").replace("[","").replace("]",""))