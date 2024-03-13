n = int(input())
mat = [[]]*n

for i in range(n):
    mat[i]=tuple(map(int,input().split()))

calc_times = [-1]*n

calc_times[0]=0
calc_times[1]=mat[0][0]*mat[1][0]*mat[1][1]
calc_times[2]=min(calc_times[1]+mat[0][0]*mat[2][0]*mat[i][1],mat[0][0]*mat[1][0]*mat[2][1]+mat[1][0]*mat[2][0]*mat[2][1])
for i in range(3,n):
    calc_times[i]=min(calc_times[i-1]+mat[0][0]*mat[i][0]*mat[i][1],calc_times[i-2]+mat[i-1][0]*mat[i][0]*mat[i][1])
print(calc_times[n-1])