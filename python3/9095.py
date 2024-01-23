import sys
input = sys.stdin.readline

t = int(input())

lists=[]

for i in range(t):
    lists.append(int(input()))
    
calc=[0]*(max(lists)+1)

calc[1]=1
calc[2]=2
calc[3]=4

for i in range(4, max(lists)+1):
    calc[i]=calc[i-1]+calc[i-2]+calc[i-3]
    
for i in lists:
    print(calc[i])