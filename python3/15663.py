from collections import deque
n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))

answer = deque()
for i in range(len(a)):
    answer.append([i])

for i in range(1,m):
    temp_answer = []
    while len(answer)!=0:
        temp = answer.popleft()
        for j in range(len(a)):
            if j not in temp:
                temp_answer.append(temp+[j])
    answer = deque(temp_answer.copy())

temp_set = set()
for i in list(answer):
    temp = i.copy()
    for j in range(len(temp)):
        temp[j]=a[temp[j]]
    temp_set.add(tuple(temp))
print(str(sorted(list(temp_set))).replace(",)",")").replace("], [","\n").replace("), (","\n").replace(", "," ").replace("]","").replace("[","").replace(")","").replace("(",""))
