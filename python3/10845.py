import sys
input = sys.stdin.readline

n = int(input())

front=0
queue=[]

for i in range(n):
    command=input()
    if command.split()[0]=="push":
        queue.append(int(command.split()[1]))
        front=front+1
    elif command.split()[0]=="pop":
        if front==0:print(-1)
        else:
            print(queue[0])
            del queue[0]
            front=front-1
    elif command.split()[0]=="size":
        print((front))
    elif command.split()[0]=="empty":
        if front==0:print(1)
        else:print(0)
    elif command.split()[0]=="back":
        if front==0:print(-1)
        else:print(queue[front-1])
    elif command.split()[0]=="front":
        if front==0:print(-1)
        else:print(queue[0])
        
        
        
    