import sys
input = sys.stdin.readline

t = int(input())

fibo_list_0 = [-1]*41
fibo_list_1 = [-1]*41

test_case = [0]*t

for i in range(t):
    test_case[i]=int(input())

fibo_list_0[0]=1
fibo_list_0[1]=0

fibo_list_1[1]=1
fibo_list_1[0]=0

for i in range(2,max(test_case)+1):
    fibo_list_0[i]=fibo_list_0[i-1]+fibo_list_0[i-2]
    fibo_list_1[i]=fibo_list_1[i-1]+fibo_list_1[i-2]



for i in range(t):
    print(fibo_list_0[test_case[i]],fibo_list_1[test_case[i]])

