import sys
input = sys.stdin.readline

n = int(input())
stair = []
max_score = []

for i in range(n):
    stair.append(int(input()))

for i in range(n):
    if i==0:#1st stair
        max_score.append(stair[i])
    elif i==1:#2nd stair
        max_score.append(stair[i-1]+stair[i])
    elif i==2:#3nd stair
        max_score.append(max(stair[i-1]+stair[i],stair[i-2]+stair[i]))
    else:
        max_score.append(max(max_score[i-3]+stair[i-1]+stair[i],max_score[i-2]+stair[i]))
        
print(max_score[n-1])