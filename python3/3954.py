'''
힌트: 
1. 프로그램이 명령어를 50,000,000번 이상 수행한 경우, 프로그램은 항상 종료되었거나 무한 루프에 빠져있다. 
->50,000,000번 이상에서 무한루프가 갑자기 유한 루프가 되는 경우는 없다.
2. 무한 루프일 경우, 해당 루프는 적어도 한 번 실행이 완료된 상태이며, 한 번의 무한 루프에서 실행되는 명령어의 개수는 50,000,000개 이하이다.
-> 무한루프의 주기는 50,000,000이하이다.

=>50,000,000 회 이상에서, PC 카운터가 도는 범위가 무한루프의 범위이다.
그리고 매번 새로 찾으면 느리니까 [] 짝은 따로 저장해 둘것

'''

MAX_LOOP = 50000000
# MAX_LOOP = 65536

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
    loop_spare= [-1]*(s_c+1)
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

                if pc_times>=MAX_LOOP:#무한루프 테스트
                    loop_test[temp]+=1#끝점에 루프 카운트 저장
                    for i in reversed(range(len(loop_test))):
                        if loop_test[i] != 0:
                            if i==temp:
                                strs="Loops "+str(pc)+" "+str(temp)
                            break

        elif program[pc]=='.':
            pc=pc#do noting
        elif program[pc]==',':
            if len(pro_input)!=0:
                memory[pointer]=int(pro_input.pop(0).encode().hex(),16)
            else:
                memory[pointer]=255
        # print(pc)
        if pc_times>int(MAX_LOOP * 2):
            break
        pc_times+=1
        pc+=1
    if pc_times<MAX_LOOP:
        strs="Terminates"
    print(strs)
