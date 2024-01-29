import math
n = int(input())


queen = [-1]*n
#queen[1]=1이다 -> queen 은 (1,1)에 있다
    

answer = 0

def queenTest(row):
    global answer
    
    for j in range(row):
        if j+queen[j]==row+queen[row]:
            return
        if j-queen[j]==row-queen[row]:
            return
                
    
    if row == n-1:
        answer = answer + 1
        return
    for i in range(n):
        triger = True
        
        if i in queen:
            continue
                
        queen[row+1]=i
        queenTest(row+1)
        queen[row+1]=-1
    


for i in range(n):
    queen[0]=i
    queenTest(0)
    queen[0]=-1
    
    
print(answer)