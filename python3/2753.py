temp = int(input())

if temp % 4 == 0 and temp % 100 != 0 or temp % 400 == 0:
    print(1)
else:
    print(0)