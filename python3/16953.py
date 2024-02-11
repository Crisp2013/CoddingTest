a, b = list(map(int, input().split()))


answer = 1

while True:
    print(b)
    if a == b:
        break    
    if b % 10 == 1:
        b = b // 10
        answer = answer + 1
        continue
    if b % 10 == 3 or b % 10 == 5 or b % 10 == 7 or b % 10 == 9:
        answer = -1
        break
    if a > b:
        answer = -1
        break    
    b = b // 2
    answer = answer + 1
    
print(answer)