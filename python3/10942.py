import sys
# import numpy as np
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

m = int(input())
for i in range(m):
    s, e = list(map(int, input().split()))
    len = e - s + 1
    answer = 1
    # s-=1
    # e-=1
    slices = a[s-1:s-1+len//2]
    slices2 = a[e-len//2:e]
    print(1 if slices == slices2 else 0)
