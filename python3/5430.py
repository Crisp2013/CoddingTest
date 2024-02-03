import sys
input = sys.stdin.readline

from collections import deque
t = int(input())

for i in range(t):
    p = input().rstrip()
    
    n = int(input())
    
    array = deque(map(int, input().replace(","," ").replace("[","").replace("]","").split()))
    
    flag_reverse = False
    
    flag=True
    for i in range(len(p)):
        if p[i]=='R':
            flag_reverse = not flag_reverse
                
        if p[i]=='D':
            if len(array)==0:
                print("error")
                flag=False
                break
            if flag_reverse:
                array.pop()
            else:
                array.popleft()
            
    if flag:
        if flag_reverse:
            print(str(list(reversed(array))).replace(" ",""))
        else:
            print(str(list(array)).replace(" ",""))
            
    
    
    
    