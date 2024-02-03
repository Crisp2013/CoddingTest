

n, m =list(map(int, input().split()))
           
lists = []
list_new = []
           

           
for i in range(1,n+1):
     lists.append([i])
           
now_len=1
           
while now_len!=m:
    for a in lists:
        for k in range(a[-1],n+1):
            temp = a.copy()
            temp.append(k)
            list_new.append(temp)
    lists=list_new.copy()
    list_new=[]
    now_len = now_len+1
    # print(lists)
for i in lists:
    print(str(i).replace(",","").replace("]","").replace("[",""))
        