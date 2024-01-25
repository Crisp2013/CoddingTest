


#2:(1)
#3:(2)
#4:(1)+(3)
#5:(4)
#6:(1)+(5)
#7:(2)+(6)
#8:(3)+(7)

t = int(input())

for i in range(t):
    n=int(input())
    
    lists = [0]*max(6,n+1)
    
    lists[1]=1
    lists[2]=1
    lists[3]=1
    lists[4]=2
    lists[5]=2


    for i in range(6,n+1):
        lists[i]=lists[i-1]+lists[i-5]
    print(lists[n])