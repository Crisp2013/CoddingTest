n, m = list(map(int, input().split()))

maps = [[]] * n

red = (-1, -1)
blue = (-1, -1)
goal = (-1, -1)
# n 높이 V
# m 너비 ->
for i in range(n):
    maps[i] = input().rstrip()
    for j in range(m):
        if maps[i][j] == 'B':
            blue = (i, j)
            maps[i].replace('B','.')
        if maps[i][j] == 'R':
            red = (i, j)
            maps[i].replace('R','.')
        if maps[i][j] == 'O':
            goal = (i, j)

work_list = [(red[0], red[1], blue[0], blue[1], 0)]

while len(work_list)!=0:
    temp = work_list.pop(0)
    red = (temp[0], temp[1])
    blue = (temp[2], temp[3])
    day = temp[4]
    # print(temp)
    if day >= 10:
        print(-1)
        exit()
    
    # 빨강이 파랑보다 더 오른쪽에 있으면
    # 파랑이 빨강보다 더 왼쪽에 있으면
    if red[1] > blue[1]:
        # 오른쪽으로 기울이기
        temp_flag=False
        red_temp = (red[0], red[1]) 
        for i in range(red[1], m):
            if maps[red[0]][i] == '#':
                red_temp = (red[0], i-1)
                break
            if maps[red[0]][i] == 'O':
                temp_flag = True
                red_temp = (-1,-1)
                break
        for i in range(blue[1], m):
            if maps[blue[0]][i] == '#' or (blue[0]==red_temp[0] and i==red_temp[1]):
                if red_temp[1]!=red[1] or blue[1]!=(i-1):
                    work_list.append((red_temp[0], red_temp[1], blue[0], i-1, day+1))
                break
            if maps[blue[0]][i] == 'O':
                temp_flag = False
                break
            
        if temp_flag:
            print(day+1)
            exit()

        # 왼쪽으로 기울이기
        temp_flag=True
        blue_temp = (blue[0], blue[1]) 
        for i in range(blue[1], -1, -1):
            if maps[blue[0]][i] == '#':
                blue_temp = (blue[0], i+1)
                break
            if maps[blue[0]][i] == 'O':
                temp_flag = False
                break
        if temp_flag:
            for i in range(red[1], -1, -1):
                if maps[red[0]][i] == '#' or (red[0]==blue_temp[0] and i==blue_temp[1]):
                    if blue_temp[1]!=blue[1] or red[1]!=(i+1):
                        work_list.append((red[0], i+1, blue_temp[0], blue_temp[1],  day+1))
                    break
                if maps[red[0]][i] == 'O':
                    print(day+1)
                    exit()

    # 파랑이 빨강보다 더 오른쪽에 있으면
    # 빨강이 파랑보다 더 왼쪽에 있으면
    else:
        # 오른쪽으로 기울이기
        temp_flag=True
        blue_temp = (blue[0], blue[1]) 
        for i in range(blue[1], m):
            if maps[blue[0]][i] == '#':
                blue_temp = (blue[0], i-1)
                break
            if maps[blue[0]][i] == 'O':
                temp_flag = False
                break
        if temp_flag:
            for i in range(red[1], m):
                if maps[red[0]][i] == '#' or (red[0]==blue_temp[0] and i==blue_temp[1]):
                    if blue_temp[1]!=blue[1] or red[1]!=(i-1):
                        work_list.append((red[0], i-1, blue_temp[0], blue_temp[1],  day+1))
                    break
                if maps[red[0]][i] == 'O':
                    print(day+1)
                    exit()

        # 왼쪽으로 기울이기
        temp_flag=False
        red_temp = (red[0], red[1]) 
        for i in range(red[1], -1, -1):
            if maps[red[0]][i] == '#':
                red_temp = (red[0], i+1)
                break
            if maps[red[0]][i] == 'O':
                temp_flag=True
                red_temp = (-1,-1)
                break
        for i in range(blue[1], -1, -1):
            if maps[blue[0]][i] == '#' or (blue[0]==red_temp[0] and i==red_temp[1]):
                if red_temp[1]!=red[1] or blue[1]!=(i+1):
                    work_list.append((red_temp[0], red_temp[1], blue[0], i+1, day+1))
                break
            if maps[blue[0]][i] == 'O':
                temp_flag=False
                break
        if temp_flag:
            print(day+1)
            exit()
    # 빨강이 파랑보다 더 위쪽에 있으면
    # 파랑이 빨강보다 더 아래쪽에 있으면
    if red[0] > blue[0]:
        # 위쪽으로 기울이기
        temp_flag = False
        red_temp = (red[0], red[1]) 
        for i in range(red[0], n):
            if maps[i][red[1]] == '#':
                red_temp = (i-1, red[1])
                break
            if maps[i][red[1]] == 'O':
                temp_flag = True
                red_temp = (-1,-1)
                break
        for i in range(blue[0], n):
            if maps[i][blue[1]] == '#' or (blue[1]==red_temp[1] and i==red_temp[0]):
                if red_temp[0]!=red[0] or blue[0]!=(i-1):
                    work_list.append((red_temp[0], red_temp[1], i-1, blue[1], day+1))
                break
            if maps[i][blue[1]] == 'O':
                temp_flag = False
                break
        if temp_flag:
            print(day+1)
            exit()
            
            
        # 아래쪽으로 기울이기
        temp_flag=True
        blue_temp = (blue[0], blue[1]) 
        for i in range(blue[0], -1, -1):
            if maps[i][blue[1]] == '#':
                blue_temp = (i+1, blue[1])
                break
            if maps[i][blue[1]] == 'O':
                temp_flag=False
                break
        if temp_flag:
            for i in range(red[0], -1, -1):
                if maps[i][red[1]] == '#' or (red[1]==blue_temp[1] and i==blue_temp[0]):
                    if blue_temp[0]!=blue[0] or red[0]!=(i+1):
                        work_list.append((i+1, red[1], blue_temp[0], blue_temp[1],  day+1))
                    break
                if maps[i][red[1]] == 'O':
                    print(day+1)
                    exit()

    # 파랑이 빨강보다 더 위쪽에 있으면
    # 빨강이 파랑보다 더 아래쪽에 있으면
    else:
        # 위쪽으로 기울이기
        temp_flag=True
        blue_temp = (blue[0], blue[1]) 
        for i in range(blue[0], n):
            if maps[i][blue[1]] == '#':
                blue_temp = (i-1, blue[1])
                break
            if maps[i][blue[1]] == 'O':
                temp_flag=False
                break
        if temp_flag:
            for i in range(red[0], n):
                if maps[i][red[1]] == '#' or (red[1]==blue_temp[1] and i==blue_temp[0]):
                    if blue_temp[0]!=blue[0] or red[0]!=(i-1):
                        work_list.append((i-1, red[1], blue_temp[0], blue_temp[1],  day+1))
                    break
                if maps[i][red[1]] == 'O':
                    print(day+1)
                    exit()

        # 아래쪽으로 기울이기
        temp_flag=False
        red_temp = (red[0], red[1]) 
        for i in range(red[0], -1, -1):
            if maps[i][red[1]] == '#':
                red_temp = (i+1, red[1])
                break
            if maps[i][red[1]] == 'O':
                temp_flag=True
                red_temp = (-1,-1)
                break
        for i in range(blue[0], -1, -1):
            if maps[i][blue[1]] == '#' or (blue[1]==red_temp[1] and i==red_temp[0]):
                if red_temp[0]!=red[0] or blue[0]!=(i+1):
                    work_list.append((red_temp[0], red_temp[1], i+1, blue[1], day+1))
                break
            if maps[i][blue[1]] == 'O':
                temp_flag=False
                break
                
        if temp_flag:
            print(day+1)
            exit()



print(-1)
