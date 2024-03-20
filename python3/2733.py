t = int(input())
for i in range(t):
    program = ""
    while True:
        temp = input().rstrip()
        temp = temp.split('%')[0]
        if temp == 'end':
            break
        program = program + temp

    s_m = 32768
    s_c= len(program)
    
    memory = [0]*(s_m)
    pointer = 0
    
    print("PROGRAM #"+str(i+1)+":")
    #괄호 유효성 검사
    pc = 0
    depth=0
    while pc!=s_c:
        if program[pc]=='[':
            depth += 1
        elif program[pc]==']':
            depth -=1
        if depth<0:#]]][[[라던지 방지
            break
        pc+=1
    if depth != 0:
        print("COMPILE ERROR")
        continue


    pc = 0
    depth=0
    loop_spare = [-1]*s_c
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
                if loop_spare[pc] == -1:#짝을 못찾음
                    while True:
                        pc+=1
                        if program[pc]=='[':
                            depth+=1
                        elif program[pc]==']':
                            depth-=1
                        if depth == 0:
                            break
                    loop_spare[temp]=pc
                    loop_spare[pc]=temp
                else:
                    pc = loop_spare[pc]
        elif program[pc]==']':#loop
            temp = pc
            depth=-1
            if memory[pointer]!=0:
                if loop_spare[pc] == -1:#짝을 못찾음
                    while True:
                        pc-=1
                        if program[pc]=='[':
                            depth+=1
                        elif program[pc]==']':
                            depth-=1
                        if depth == 0:
                            break
                    loop_spare[temp]=pc
                    loop_spare[pc]=temp
                else:
                    pc = loop_spare[pc]

        elif program[pc]=='.':
            print(chr(memory[pointer]),end='')
        # elif program[pc]==',':
        #     if len(pro_input)!=0:
        #         memory[pointer]=int(pro_input.pop(0).encode().hex(),16)
        #     else:
        #         memory[pointer]=255

        pc+=1
    print()

