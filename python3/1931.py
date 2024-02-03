import sys

input = sys.stdin.readline

n = int(input())

dictionary = dict()

max_time = 0

for i in range(n):
    s, e = list(map(int, input().split()))
    try:
        dictionary[s].appned(e)
    except:
        dictionary[s]=[e]
    max_time = max(max_time, e)

        
time = 0
task = 0
while time<=max_time:
    try:
        print(time,min(dictionary[time]))
        time = min(dictionary[time])
        task = taks+1
    except:
        time +1
        
print(task)