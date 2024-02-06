from collections import deque

a = deque(list(input()))
b = list(input())

result = deque()

# a_len = len(a)
b_len = len(b)

while len(a)!=0:
    
    bomb = True
    if len(a)>=b_len:
        for i in range(b_len):
            if a[i]!=b[i]:
                bomb = False
                break

        if bomb:
            for i in range(b_len):
                a.popleft()

            for i in range(min(b_len, len(result))):
                a.appendleft(result.pop())
            continue

    result.append(a.popleft())
        

if result!=deque():
    print(''.join(list(result)))
else:
    print("FRULA")