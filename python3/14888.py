n = int(input())
a = list(map(int, input().split()))
p,m,t,d = list(map(int, input().split()))

max_value = -10e9
min_value = 10e9

work_list = [(0,p,m,t,d,a[0])]
while len(work_list) != 0:
    current = work_list.pop(-1)
    # print(current)    

    if current[0]+1 == n:
        max_value = max(current[5],max_value)
        min_value = min(current[5],min_value)
        continue
    next_input = a[current[0]+1]

    if current[1]!=0:
        work_list.append((current[0]+1,current[1]-1,current[2],current[3],current[4],current[5]+next_input))
    if current[2]!=0:
        work_list.append((current[0]+1,current[1],current[2]-1,current[3],current[4],current[5]-next_input))
    if current[3]!=0:
        work_list.append((current[0]+1,current[1],current[2],current[3]-1,current[4],current[5]*next_input))
    if current[4]!=0:
        work_list.append((current[0]+1,current[1],current[2],current[3],current[4]-1,-(abs(current[5])//next_input) if current[5] < 0 else (current[5]//next_input)))

print(max_value)
print(min_value)