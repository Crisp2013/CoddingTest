import sys
input = sys.stdin.readline

m = int(input())
lists = set([])
for i in range(m):
    opcode = input().split()
    
    if opcode[0]=="add":
        lists.add(int(opcode[1]))
    elif opcode[0]=="remove":
        if int(opcode[1]) in lists:
            lists.remove(int(opcode[1]))
    elif opcode[0]=="check":
        if int(opcode[1]) in lists: print(1)
        else: print(0)
    elif opcode[0]=="toggle":
        if int(opcode[1]) in lists: lists.remove(int(opcode[1]))
        else: lists.add(int(opcode[1]))
    elif opcode[0]=="all":
        lists=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif opcode[0]=="empty":
        lists = set([])