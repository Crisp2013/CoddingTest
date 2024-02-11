import math

#최소 공약수 함수로 만들어 줘야됨
def lcm(a,b):
  return (a * b) // math.gcd(a,b)

m = int(input())

maps = [[]]*m

X = 1000000007
# X = 11

for i in range(m):
    maps[i] = list(map(int, input().split()))

#고속 거듭제곱 + 모듈러(모듈러는 곱셈에 대해 항등?)
def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 !=0:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result

def modular_e(a, b):
    # i = 1
    # while True:
    #     if ((X * i)+1) % b == 0:
    #         break
    #     i = i + 1
    # return (((X * i)+1)//b*a) % X
    #TODO: 거듭제곱을 분할 정복으로 계산해야함(dp 이용?)
    # return (((b ** (X-2)) % X)*a) % X
    return (power(b,X-2,X) * a) % X

def modular_d(c, b):
    return (c*b) % X


temp_b = maps[0][0]
temp_a = modular_e(maps[0][1], temp_b)


for i in range(1, m):
    b_t = lcm(maps[i][0], temp_b)
    
    # temp_a = modular_e(maps[i][1]*(b_t//temp_b)+modular_d(temp_a, b_t),b_t)
    temp_a = (modular_e(maps[i][1], maps[i][0])+temp_a) % X
    temp_b = b_t
    
# print(modular_d(temp_a,temp_b))
# print(temp_b)
print(temp_a)



