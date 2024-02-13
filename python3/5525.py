n = int(input())
m = int(input())
s = input()

answer = 0
# for i in range(m-n*2):
#     for j in range(n*2+1):
#         if j%2==0:
#             if s[i+j]!="I":
#                 break
#         else:
#             if s[i+j]!="O":
#                 break
#         if j==n*2:
#             answer = answer + 1
lists = []
start = 0
lenth = 0
i = 0
while i<m:
    if lenth == 0:
        start=i
    if lenth%2 == 0:
          if s[i]=='I':
            lenth = lenth + 1
            i = i + 1
            continue
    else:
          if s[i]=='O':
            lenth = lenth + 1
            i = i + 1
            continue
    lists.append(s[start:start+lenth])
    if lenth == 0:
        i = i + 1
    lenth = 0
    
lists.append(s[start:start+lenth])
# print(lists)   
for arr in lists:
    answer = answer + max((len(arr)+1)//2-n, 0)


 
          

print(answer)