t = input()

for i in range(int(t)):
    a=input().split()
    
    for j in range(len(a[1])):
        for k in range(int(a[0])):
            print(a[1][j], end="")
    print("")