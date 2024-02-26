from collections import deque
n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))

answer = deque()
for i in a:
    answer.append([i])

for i in range(1,m):
    temp_answer = []
    while len(answer)!=0:
        temp = answer.popleft()
        for j in a:
            if j not in temp:
                temp_answer.append(temp+[j])
    answer = deque(temp_answer.copy())
print(str(list(answer)).replace("], [","\n").replace(", "," ").replace("]","").replace("[",""))
