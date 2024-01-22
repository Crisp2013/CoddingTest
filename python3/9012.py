n = int(input())

word_list=[]

for i in range(n):
    word=input()
    a=0
    for j in range(len(word)):
        if word[j] == '(': a=a+1
        if word[j] == ')': a=a-1
        if a<0:
            break
    if a!=0:
        print("NO")
    else:
        print("YES")
        