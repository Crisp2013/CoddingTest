'''
    힌트: 문자열에서 팰랜드롬을 확인하는 방법은
    1,2글자를 점화식의 초기항으로 하고
    3글자이상부터 점화식으로 판별한다.
    점화식:  if [i+1][j-1] and string[i]==string[j]:  [i][j] = True
'''
string = input()
length = len(string)

INF = int(200000)

test = [[False for i in range(length)] for i in range(length)]

#1글자짜리: 전부 팰린드롬
for i in range(length):
    test[i][i]=True
#2글짜짜리
for i in range(length-1):
    if string[i]==string[i+1]:
        test[i][i+1]=True
#3글자 이상
for l in range(2, length):
    for i in range(length - l):
        j = i + l 
        
        if test[i+1][j-1]==1 and string[i]==string[j]:
            test[i][j] = True

#팰랜드롬 여부 확인 완료
            
#여기가 DP임...
#DP는 항상 1차원으로 생각할것
# 요약: 어쨋든 [K,N]이 팰랜드롬이면 [0,K-1]의 팰랜드롬 조합의 최솟값에 +1을 더하면 무조껀 된다. 이거 걍 그리디 아님?
fallenmin = [INF]*length
for i in range(length):
    #0~i가 팰랜드롬이면?
    if test[0][i] == True:
        # print("test")
        fallenmin[i]=1
    else:
        for j in range(i):
            #J+1~I가 팰랜드롬이면?
            if test[j+1][i] == True:
                fallenmin[i] = min(fallenmin[j]+1,fallenmin[i])
# I=1
# J=0 -> 0,0 1,1
# print(fallenmin)
# for i in range(length):
#     for j in range(length):
#         if test[i][j] == INF:
#             test[i][j] = 0
# for i in range(length):
#     print(test[i])
print(fallenmin[length-1])

#