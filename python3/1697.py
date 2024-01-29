n, k = list(map(int, input().split()))


visited = set([n])

work_list = [(0, n)]

while True:
    times, pos = work_list.pop(0)
    
    # if pos > max(n,k*2):
    #     continue
    # if pos < min(n,k//2):
    #     continue
    
    if pos==k:
        print(times)
        exit()
    
    
    if pos+1 not in visited and pos+1<=100000:
        work_list.append((times+1,pos+1))
        visited.add(pos+1)
    if pos-1 not in visited and pos-1>=0:
        work_list.append((times+1,pos-1))
        visited.add(pos-1)
    if pos*2 not in visited and pos*2<=100000:
        work_list.append((times+1,pos*2))
        visited.add(pos*2)
    