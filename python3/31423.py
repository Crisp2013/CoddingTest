import sys
input = sys.stdin.readline
n = int(input())
temp = [""]*(n+1)

for i in range(1,n+1):
    temp[i]=input().rstrip()

tem = -1
for i in range(n-1):
    sets = list(map(int, input().split()))
    temp[sets[0]]=temp[sets[0]]+temp[sets[1]]
    temp[sets[1]]=""
    tem = sets[0]

print(temp[tem])