import sys

n = int(input())

input = sys.stdin.readline

lists = []

for i in range(n):
    (x, y) = list(map(int, input().split()))
    lists.append([x, y])
    
lists = sorted(lists, key=lambda lists: lists[1])
lists = sorted(lists, key=lambda lists: lists[0])


for i in range(n):
    print(lists[i][0], lists[i][1])
    