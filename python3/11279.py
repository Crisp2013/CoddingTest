import sys
input = sys.stdin.readline
import heapq

arr = []

n = int(input())
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-(heapq.heappop(arr)))
    else:
        heapq.heappush(arr,-temp)