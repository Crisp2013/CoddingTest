from collections import deque
import sys

n = sys.stdin.readline().split()[0]

a = deque(range(1, int(n)+1))

while len(a)!=1:
    a.popleft()
    a.append(a.popleft())
    

print(a[0])