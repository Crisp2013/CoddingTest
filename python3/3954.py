t = int(input())
for i in range(t):
    s_m, s_c, s_i = list(map(int, input().split()))
    program = input().rstrip()
    pro_input = list(input().rstrip())
    memory = [0]*s_m
    pointer = 0
    pc = 0
    strs="Terminates"
    pc_times = 0
    loop_test = dict()
    while pc!=s_c:
        if program[pc]=='-':
            memory[pointer] = (memory[pointer]-1)%256
        elif program[pc]=='+':
            memory[pointer] = (memory[pointer]+1)%256
        elif program[pc]=='<':
            pointer-=1
        elif program[pc]=='>':
            pointer+=1
        elif program[pc]=='[':
            temp = pc
            depth=1
            if memory[pointer]==0:
                while True:
                    pc+=1
                    if program[pc]=='[':
                        depth+=1
                    elif program[pc]==']':
                        depth-=1
                    if depth == 0:
                        break
                    
                try:
                    loop_test[(temp,pc)]+=1
                    # print(loop_test[(temp,pc+1)])
                except:
                    loop_test[(temp,pc)]=0
                if loop_test[(temp,pc)]>40000000:
                    strs="Loops"+str(temp)+str(pc)
                    break
        elif program[pc]==']':
            temp = pc
            depth=-1
            if memory[pointer]!=0:
                while True:
                    pc-=1
                    if program[pc]=='[':
                        depth+=1
                    elif program[pc]==']':
                        depth-=1
                    if depth == 0:
                        break
                try:
                    loop_test[(pc,temp)]+=1
                    # print(loop_test[(pc,temp+1)])
                except:
                    loop_test[(pc,temp)]=0
                if loop_test[(pc,temp)]>40000000:
                    strs="Loops"+str(pc)+str(temp)
                    break
        elif program[pc]=='.':
            # print(memory[pointer])
            pc=pc#do noting
        elif program[pc]==',':
            if len(pro_input)!=0:
                memory[pointer]=int(pro_input.pop().encode().hex(),16)
            else:
                memory[pointer]=255
        # print(pc)
        if pc_times>=50000000:
            break
        pc_times+=1
        pc+=1
    print(strs)
