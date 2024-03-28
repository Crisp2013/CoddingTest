s, e = list(map(int, input().split()))

sums = 0
for i in range(s,e+1):
    sums += sum(list(map(int, bin(i).replace("0b",""))))
print(sums)
