# MAX_LOOP = 50000002
# MAX_LOOP = 565536
MAX_LOOP = 65536

t = int(input())
for i in range(t):
    s_m, s_c, s_i = list(map(int, input().split()))
    program = input().rstrip()
    pro_input = list(input().rstrip())
    memory = [0]*(s_m+1)
    pointer = 0
    pc = 0
    strs="Terminates"
    pc_times = 0
    loop_test = [0]*(s_c+1)
    while pc!=s_c:
        if program[pc]=='-':
            memory[pointer] = (memory[pointer]-1)%256
        elif program[pc]=='+':
            memory[pointer] = (memory[pointer]+1)%256
        elif program[pc]=='<':
            pointer=(pointer-1)%s_m
        elif program[pc]=='>':
            pointer=(pointer+1)%s_m
        elif program[pc]=='[':#jump
            temp = pc
            depth=1
            if memory[pointer]==0:
                loop_clear=[]
                while True:
                    pc+=1
                    if program[pc]=='[':
                        depth+=1
                    elif program[pc]==']':
                        depth-=1
                    if depth == 0:
                        break
                # loop_test[pc]=0#무한루프가 아님(탈출함)
        elif program[pc]==']':#loop
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
                # try:
                loop_test[temp]+=1#끝점에 루프 카운트 저장
                # except:
                    # loop_test[temp]=0
                if loop_test[temp] == max(loop_test):
                    strs="Loops "+str(pc)+" "+str(temp)
                # for i in reversed(range(len(loop_test))):
                #     if loop_test[i] != 0:
                #         if i==temp:
                #             strs="Loops "+str(pc)+" "+str(temp)
                #         break

                # if loop_test[temp]>=MAX_LOOP:
                #     break
            else:
                # print(loop_test[temp])
                temp_val = loop_test[temp]
                # loop_test[temp]=0#무한루프가 아님(탈출함)
                for i in range(temp,len(loop_test)):
                    if loop_test[i]!=0:
                       loop_test[i]+= temp_val

        elif program[pc]=='.':
            # print(memory[pointer])
            pc=pc#do noting
        elif program[pc]==',':
            if len(pro_input)!=0:
                memory[pointer]=int(pro_input.pop().encode().hex(),16)
            else:
                memory[pointer]=255
        # print(pc)
        if pc_times>=MAX_LOOP:
            break
        pc_times+=1
        pc+=1
        # if pc_times%(MAX_LOOP//10) == 0:
        #     print(loop_test)
    if pc_times<MAX_LOOP:
        strs="Terminates"
    print(strs)
