import sys
'''
    힌트: 해당 문제는 트리다!
'''
N = int(input())

miro = dict()
#miro[n][0]: 부모
#miro[n][1...]: 자식
for i in range(1,N+1):
    miro[i]=[-1]
miro[1]=[0]#루트

cur = 1 # 현재 위치
known = 1 #위치가 알려진 정점 수

isFirst = True

def posfunc(opcode):
    print(opcode)
    sys.stdout.flush()
    return int(input())

while True:
    if isFirst:
        isFirst = False
        new_pos = posfunc("maze")
    
    if known==N:
        break
    if miro[new_pos][0] == -1: #방문하지 않은 정점일경우?
        miro[new_pos][0] = cur #new_pos에 부모노드 기록
        miro[cur].append(new_pos)#cur에 자식노드 기록
        known+=1
        cur=new_pos
        new_pos = posfunc("maze")
    else:#이미 방문한 정점일 경우?
        #cur 노드의 탐색은 끝난 것이므로 그냥 끝낸다.
        if miro[cur][0]==new_pos: #만약에 부모노드로 온 경우
            cur=new_pos
            new_pos = posfunc("maze")#새로 탐색하죠
        else:#부모노드로 오지 않은 경우
            cur=new_pos
            new_pos = posfunc("gaji "+str(miro[cur][0]))#해당 노드를 다시 벗어날것(다시 부모노드로)
            cur=new_pos
            if miro[cur][0] == 0:#루트?
                break
            new_pos = posfunc("gaji "+str(miro[cur][0]))#부모노드로 돌아갈것(해당 노드 탐색 종료)
            cur=new_pos
            new_pos = posfunc("maze")#새로 탐색하죠

    # for i in range(1,N+1):
    #     print(i, miro[i])

print("answer")
for i in range(1,N+1):
    for j in range(1,len(miro[i])):
        print(i, miro[i][j])
        sys.stdout.flush()


    
    

