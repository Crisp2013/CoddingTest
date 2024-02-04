n = int(input())

x = list(map(int, input().split()))

x_s = sorted(list(set(x)))

maps = dict()
a = 0
for i in x_s:
    maps[i]=a
    a = a + 1

for i in range(n):
    x[i]=maps[x[i]]

print(str(x).replace(',','').replace(']','').replace('[',''))