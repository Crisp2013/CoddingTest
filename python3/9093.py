n = int(input())
for i in range(n):
    temp = input().split()
    for k in temp:
        print(''.join(reversed(list(k))), end=' ')
    print()