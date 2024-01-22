import sys
input = sys.stdin.readline

(n,k)=list(map(int,input().split()))

top=1
bottom = 1
for t in range (n-k+1, n+1):
    top = top * t
for t in range (1, k+1):
    bottom = bottom * t
    

print (top//bottom)
