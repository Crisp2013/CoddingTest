import sys
input = sys.stdin.readline

n = input()
p = sorted(list(map(int, input().split())))

answer = 0

for i in range(len(p)):
    answer = answer + sum(p[0:i+1])
print(answer)
