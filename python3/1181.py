n = int(input())

word_list=[]

for i in range(n):
    word=input()
    word_list.append((len(word),word))

word_list=sorted(word_list, key=lambda word_list:word_list[1])
word_list=sorted(word_list, key=lambda word_list:word_list[0])

temp=""
for i in range(n):
    if temp!=word_list[i][1]:
        print(word_list[i][1])
    temp=word_list[i][1]
