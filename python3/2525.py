temp = list(map(int, input().split()))

temp2 = int(input())

temp[0]=(temp[0]+(temp[1]+temp2)//60)%24
temp[1]=(temp[1]+temp2)%60


print(temp[0], temp[1])