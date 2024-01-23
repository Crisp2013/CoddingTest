import sys
from collections import deque
input = sys.stdin.readline

n,k=list(map(int, input().split()))

coin_val = [0] * n

count = 0
for i in range(n):
    coin_val[i]=int(input())

for i in range(n-1, -1, -1):
    if True:
         temp = k // coin_val[i]
         count = count + temp
         k=k-temp*coin_val[i]
         
print(count)
    

