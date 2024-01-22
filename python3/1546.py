import sys

n = int(input())

input = sys.stdin.readline

lists = list(map(int, input().split()))

print(sum(lists)/n*100/max(lists))