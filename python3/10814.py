n = int(input())

word_list=[]

for i in range(n):
    (val,word)=input().split()
    word_list.append((int(val),word))

word_list=sorted(word_list, key=lambda word_list:word_list[0])

for i in range(n):
    print(word_list[i][0],word_list[i][1])
