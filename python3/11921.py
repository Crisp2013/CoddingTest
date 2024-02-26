from collections import deque
import sys
input = sys.stdin.readline
test =  1
n = int(input())
answer_sum = deque()
for i in range(min(test,n)):
    answer_sum.append(int(input()))

print(min(test,n))
print(sum(answer_sum))
