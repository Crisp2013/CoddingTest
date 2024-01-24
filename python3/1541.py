a=list(input()+"!")

calc_v=[]
calc_t=['+']

start=-1
while True:
    if start!=-1:
        if a[start] =='!':
            break
        calc_t.append(a[start])



    if a[start+2] == '+' or a[start+2] == '-' or a[start+2] =='!':
        calc_v.append(int(''.join(a[start+1:start+2])))
        start=start+2
    elif a[start+3] == '+' or a[start+3] == '-' or a[start+3] =='!':
        calc_v.append(int(''.join(a[start+1:start+3])))
        start=start+3
    elif a[start+4] == '+' or a[start+4] == '-' or a[start+4] =='!':
        calc_v.append(int(''.join(a[start+1:start+4])))
        start=start+4
    elif a[start+5] == '+' or a[start+5] == '-' or a[start+5] =='!':
        calc_v.append(int(''.join(a[start+1:start+5])))
        start=start+5
    elif a[start+6] == '+' or a[start+6] == '-' or a[start+6] =='!':
        calc_v.append(int(''.join(a[start+1:start+6])))
        start=start+6

# print(calc_v)
# print(calc_t)

sum_temp=0
answer=0

for i in range(len(calc_v)-1,-1,-1):
    sum_temp=sum_temp + calc_v[i]
    if calc_t[i]=='-':
        answer=answer-sum_temp
        sum_temp=0
answer=answer+sum_temp

print(answer)

