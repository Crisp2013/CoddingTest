n, b = list(map(int, input().split()))

a = [[]] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

answer = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    answer[i][i] = 1

# print (answer)
def cal_mat(x,y):
    z = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i][j]= (z[i][j] + x[i][k]*y[k][j])%1000
    return z


while b > 0:
    if b % 2 == 1:
        answer = cal_mat(a, answer)
    a = cal_mat(a, a)
    b = b // 2

print(str(answer).replace("], [","\n").replace(",","").replace("[","").replace("]",""))