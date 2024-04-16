import sys
input = sys.stdin.readline

n, l = list(map(int, input().split()))
a = [[]]*n
for i in range(n):
    a[i] = list(map(int, input().split()))

#걍 SUM으로 구할래... True sum해도 1로 변환되나?
flag_v = [1]*n
flag_h = [1]*n

for i in range(n):
    v_temp_set = [0]*n
    j=0
    while j<n:
        current = a[i][j]
        if current != a[i][min(j+l,n-1)]:#L칸 이후에 높이가 다를때!
            if abs(current-a[i][min(j+l,n-1)])>=2: #두칸이상 차이면!
                flag_v[i]=0#포기해라
                break
        j+=1
    if flag_v[i] == 0:
        continue
        
    j=0
    while j<n:
        current = a[i][j]
        if current != a[i][min(j+l,n-1)]:#L칸 이후에 높이가 다를때!
            if current + 1<a[i][min(j+l,n-1)]: #두칸이상 차이면!
                flag_v[i]=0#포기해라
                break
            elif current > a[i][min(j+l,n-1)]: #오히려 더 낮으면!
                j+=1
                continue#역방향 검색에서 처리할예정
            else:#딱 1높을때
                for k in range(j+1,min(j+l,n-1)):#그 사이 검색
                    if a[i][k] != current: #요철이 있음?
                        flag_v[i]=0#포기해라
                        break
                for k in range(j,min(j+l,n-1)):
                    v_temp_set[k]=1
                j+=l
        else:
            for k in range(j+1,min(j+l,n-1)):#그 사이 검색
                if a[i][k] != current: #요철이 있음?
                    flag_v[i]=0#포기해라
                    break
            j+=1
        if flag_v[i] == 0:
            break
    if flag_v[i] == 0:
        continue
    
    j=n-1
    while j>=0:
        current = a[i][j]
        if current != a[i][max(j-l,0)]:#L칸 이후에 높이가 다를때!
            if current + 1<a[i][max(j-l,0)]: #두칸이상 차이면!
                flag_v[i]=0#포기해라
                break
            elif current > a[i][max(j-l,0)]: #오히려 더 낮으면!
                j-=1
                continue#역방향 검색에서 처리할예정
            else:#딱 1높을때
                for k in range(max(j-l,0)+1,max(j-1,0)+1):#그 사이 검색
                    if a[i][k] != current: #요철이 있음?
                        flag_v[i]=0#포기해라
                        break
                if sum(v_temp_set[max(j-l,0)+1:j+1])>0:
                        flag_v[i]=0#포기해라
                        break
                j-=l
        else:
            for k in range(max(j-l,0)+1,max(j-1,0)+1):#그 사이 검색
                if a[i][k] != current: #요철이 있음?
                    flag_v[i]=0#포기해라
                    break
            j-=1
        if flag_v[i] == 0:
            break
for i in range(n):
    h_temp_set = [0]*n
    j=0
    while j<n:
        current = a[j][i]
        if current != a[min(j+l,n-1)][i]:#L칸 이후에 높이가 다를때!
            if abs(current-a[min(j+l,n-1)][i])>=2: #두칸이상 차이면!
                flag_h[i]=0#포기해라
                break
        j+=1
    if flag_h[i] == 0:
        continue

    j=0
    while j<n:
        current = a[j][i]
        if current != a[min(j+l,n-1)][i]:#L칸 이후에 높이가 다를때!
            if current + 1<a[min(j+l,n-1)][i]: #두칸이상 차이면!
                flag_h[i]=0#포기해
                break
            elif current > a[min(j+l,n-1)][i]: #오히려 더 낮으면!
                j+=1
                continue#역방향 검색에서 처리할예정
            else:#딱 1높을때
                for k in range(j+1,min(j+l,n-1)):#그 사이 검색
                    if a[k][i] != current: #요철이 있음?
                        flag_h[i]=0#포기해라
                        break
                for k in range(j,min(j+l,n-1)):
                    h_temp_set[k]=1
                j+=l
        else:
            for k in range(j+1,min(j+l,n-1)):#그 사이 검색
                if a[k][i] != current: #요철이 있음?
                    flag_h[i]=0#포기해라
                    break
            j+=1
        if flag_h[i] == 0:
            break
    if flag_h[i] == 0:
        # print("skip",i)
        continue
    
    j=n-1
    while j>=0:
        # print(j)
        # print(a[j][i],a[max(j-l,0)][i])
        current = a[j][i]
        if current != a[max(j-l,0)][i]:#L칸 이후에 높이가 다를때!
            if current + 1 < a[max(j-l,0)][i]: #두칸이상 차이면!
                # print(current, a[j-l][i])
                # print(j)
                flag_h[i]=0#포기해라
                # print("예")
                break
            elif current > a[max(j-l,0)][i]: #오히려 더 낮으면!
                j-=1
                continue#역방향 검색에서 처리할예정
            else:#딱 1높을때
                for k in range(max(j-l,0)+1,max(j-1,0)+1):#그 사이 검색
                    if a[k][i] != current: #요철이 있음?
                        flag_h[i]=0#포기해라
                        break
                if sum(h_temp_set[max(j-l,0)+1:j+1])>0:
                        flag_h[i]=0#포기해라
                        break
                j-=l
        else:
            for k in range(max(j-l,0)+1,max(j-1,0)+1):#그 사이 검색
                if a[k][i] != current: #요철이 있음?
                    flag_h[i]=0#포기해라
                    break
            j-=1
        if flag_h[i] == 0:
            break
# print(flag_v)#1번째가 고정일때
# print(flag_h)#2번째가 고정일때
print(sum(flag_h)+sum(flag_v))