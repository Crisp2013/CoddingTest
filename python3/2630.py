import sys
input = sys.stdin.readline

n = int(input())

paper = [[]] * n

for i in range(n):
    paper[i]=list(map(int, input().split()))
white = 0
blue = 0
# 크기가 1이다 이러몀ㄴ 0, 1로 입력디게
def check_paper (x1, x2, y1, y2):
    global blue
    global white
    sum_temp = 0
    
    for i in range(x1, x2):
        sum_temp = sum_temp+sum(paper[i][y1:y2])
    wh = x2-x1
    if sum_temp == 0:
        print(x1, x2, y1, y2)
        white = white + 1
    elif sum_temp == wh ** 2:
        print(x1, x2, y1, y2)
        blue = blue + 1
    else:
        check_paper(x1, x1+wh//2, y1, y1+wh//2)
        check_paper(x1+wh//2, x1+wh, y1, y1+wh//2)
        check_paper(x1, x1+wh//2, y1+wh//2, y1+wh)
        check_paper(x1+wh//2, x1+wh, y1+wh//2, y1+wh)
        
check_paper(0,n,0,n)
print(white)
print(blue)