n = int(input())

a = list(map(int, input().split()))
b, c = list(map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i]=max(-1,(a[i]-b-1))//c+1+1
print(sum(d))