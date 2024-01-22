(n,m)=list(map(int,input().split()))

board=[]
type1="WBWBWBWB"
type2="BWBWBWBW"

def count_not_same(a,b,k):
    c=0
    for i in range(8):
        if a[i+k]!=b[i]:c=c+1
    return c

for i in range(n):
    board.append(input())
min_val=123548973
for i in range(n-8+1):
    a=board[i:i+8]
    
    for k in range(m-8+1):
        type1_count=0
        type2_count=0
        for j in range(8):
            if j%2==0:
                type1_count=count_not_same(a[j],type1,k)+type1_count
                type2_count=count_not_same(a[j],type2,k)+type2_count
            else:
                type1_count=count_not_same(a[j],type2,k)+type1_count
                type2_count=count_not_same(a[j],type1,k)+type2_count
        
        temp=min((type1_count,type2_count))
        if temp<min_val:min_val=temp
print(min_val)
    
