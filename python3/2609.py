import sys
input = sys.stdin.readline

(a, b) = list(map(int, input().split()))


for i in range(min(a, b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break
i=1    
while True:
    if (max(a,b)*i)%min(a,b)==0:
        print(max(a,b)*i)
        break
    i=i+1