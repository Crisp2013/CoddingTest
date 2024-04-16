import sys
input = sys.stdin.readline
n = int(input())

a = [[]]*n
for i in range(n):
    a[i]= list(map(int, input().split()))

work_list = [(-1,[],[],0,0)]

min_val = 10e9
while len(work_list)!=0:
    current=work_list.pop()
    current_person = current[0]+1
    if current_person == n:
        min_val = min (min_val,abs(current[3]-current[4]))
        continue
    temp=0
    for i in current[1]:
        temp += a[i][current_person]
        temp += a[current_person][i]
    if len(current[1])+1<=n//2:
        work_list.append((current_person,current[1]+[current_person],current[2],current[3]+temp,current[4]))
    temp2=0
    for i in current[2]:
        temp2 += a[i][current_person]
        temp2 += a[current_person][i]
    if len(current[2])+1<=n//2:
        work_list.append((current_person,current[1],current[2]+[current_person],current[3],current[4]+temp2))

print(min_val)