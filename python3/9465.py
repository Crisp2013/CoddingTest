t = int(input())

for i in range(t):
    n = int(input())
    maps = [[],[]]
    maps[0]=list(map(int, input().split()))
    maps[1]=list(map(int, input().split()))

    sum = [[0 for i in range(n)] for j in range(2)]

    sum[0][0]=maps[0][0]
    sum[1][0]=maps[1][0]
    if n>=2:
        sum[0][1]=maps[0][1]+maps[1][0]
        sum[1][1]=maps[1][1]+maps[0][0]

    for i in range(2,n):
        sum[0][i]=maps[0][i]+max(sum[0][i-2],sum[1][i-2],sum[1][i-1])
        sum[1][i]=maps[1][i]+max(sum[1][i-2],sum[0][i-2],sum[0][i-1])

    print(max(sum[1][n-1],sum[0][n-1]))
    