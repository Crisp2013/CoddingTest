n, s = list(map(int, input().split()))
l  = list(map(int, input().split()))

for i in range(n-1):
    l[i+1]=l[i]+l[i+1]
l = [0]+l
start = 0
end = 0
min_len = int(10e9)
while True:
    # print(start,end)
    if l[end]-l[start]<s:
        if end == n:
            break
        end+=1
    elif l[end]-l[start]>=s:
        if start == n:
            break
        min_len = min (min_len,end-start)
        start+=1
if min_len>=int(10e9):
    min_len=0
print(min_len)