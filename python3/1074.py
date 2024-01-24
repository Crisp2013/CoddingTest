n, r, c = list(map(int, input().split()))

# 1일때
# 0 1
# 2 3
# 2일때
# 0 4
# 8 16


answer = 0

for i in range(n,0,-1):
    wh = 2**i
               
    if r < wh/2:#행
        if c < wh/2:
            answer = answer*4+0
        else:
            answer = answer*4+1
    else:#열
        if c < wh/2:
            answer = answer*4+2
        else:
            answer = answer*4+3
        
    r = r % (wh/2)
    c = c % (wh/2)
print(answer)
    