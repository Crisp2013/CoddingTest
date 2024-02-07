a, b, c = list(map(int, input().split()))

answer = 1
while b > 0:
    if b % 2 == 1:
        answer = (answer * a)
        b = b - 1
    b = b // 2
    a = a * a
    
print(answer)



