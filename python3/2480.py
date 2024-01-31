temp = list(map(int, input().split()))

if temp[0]==temp[1]==temp[2]:
    print(10000+temp[0]*1000)
elif temp[0]==temp[1]:
    print(1000+temp[0]*100)
elif temp[1]==temp[2]:
    print(1000+temp[1]*100)
elif temp[0]==temp[2]:
    print(1000+temp[0]*100)
else:
    print(max(temp)*100)