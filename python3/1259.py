import sys
input = sys.stdin.readline

while True:
    temp = input().split()[0]
    test = "yes"
    if temp == "0" : break
    for i in range(len(temp)):
        if temp[i] != temp[-1-i]: test = "no"
    print(test)