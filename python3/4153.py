import sys
input = sys.stdin.readline


while True:
    t = False
    (a, b, c) = list(map(int,input().split()))
    if a==b==c==0: break
    if a * a == b * b + c * c: t = True
    elif b * b == a * a + c * c: t = True
    elif c * c == b * b + a * a: t = True
    
    if t: print("right")
    else: print("wrong")
        
    