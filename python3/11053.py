n = int(input())
a = list(map(int, input().split()))


lists = [[a[0],1]]
lists_count = 1
for i in range(1,n):

    # print(lists)
    for task in range(lists_count+1):
        if task == lists_count:
            lists.append([a[i],1])
            lists_count = lists_count + 1
            break
        
        if a[i] > lists[task][0]:
            lists.append([a[i],lists[task][1]+1])
            lists_count = lists_count + 1
            break
            
    lists.sort(key=lambda x:-x[1])
print(lists[0][1])

#시간복잡도: N^logn