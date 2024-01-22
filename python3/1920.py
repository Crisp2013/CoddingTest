import sys
input = sys.stdin.readline

n = int(input().split()[0])

a = set(map(int, input().split()))

m = int(input().split()[0])

x = list(map(int, input().split()))

a = sorted(a)

b = 0

for i in x:
    answer=0
    
    if i<a[0] or i>a[-1]:
        print(0)
        continue
    
    if i==a[0] or i==a[-1]:
        print(1)
        continue
    start = 0
    end = len(a)
    
    while True:
        
        if end-start <= 1:
            break
        if i==a[start] or i==a[end-1] or i == a[(start+end)//2]:
            answer = 1
            break
        if i < a[(start+end)//2]:
            end = (start+end)//2
        else:
            start = (start+end)//2
    
    
    print(answer)
    

