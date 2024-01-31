t = int(input())

lists = []

for i in range(t):
    lists.append(int(input()))
    
dp1 = [0]*max(4,(max(lists)+1))
dp2 = [0]*max(4,(max(lists)+1))
dp3 = [0]*max(4,(max(lists)+1))

dp1[1]=1#1
dp2[1]=0
dp3[1]=0

dp1[2]=0
dp2[2]=1#2
dp3[2]=0


dp1[3]=1#2+1
dp2[3]=1#1+2
dp3[3]=1#3


for i in range(4,max(lists)+1):
    dp1[i]=(dp2[i-1]%1000000009+dp3[i-1]%1000000009)#+1
    dp2[i]=(dp1[i-2]%1000000009+dp3[i-2]%1000000009)#+2
    dp3[i]=(dp2[i-3]%1000000009+dp1[i-3]%1000000009)#+3

for n in lists:
    print((dp1[n]+dp2[n]+dp3[n])%1000000009)