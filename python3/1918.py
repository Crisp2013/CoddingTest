a = input()
n = len(a)


stack = []
#근본적 생각
#피연산자의 순서는 바뀌지 않는다
#연산자의 순서는 역순이 된다- > 연산자만 '스택'에 넣어 잘 순서를 정해줘서 출력을 해주면 된다.
#A+B*C -> ABC*+
#A*B+C -> AB*C+
#A*B*C -> AB*C*
#A+B+C -> AB+C+
#-> 현재 입력된 연산자가 스택에 있는 연산자 보다 우선순위가 낮거나 같은 전부다 다 출력을 해줘야 한다.
#괄호의 경우 연산자 스택에 넣어, )가 들어가면 (가 나올때 까지 다 배출해 주면 된다.)


for i in range(n):
    #괄호를 만나면 끝까지 배출
    if a[i]==')':
        while len(stack)!=0 and stack[-1] != '(':
            print(stack.pop(),end="")
        stack.pop()
        
    #우선순위 가장높은 *와 /은 *와 /만 배출
    elif a[i]=='*' or a[i]=='/':
        if len(stack)!=0:
            while len(stack)!=0 and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(),end="")
        stack.append(a[i])
    #우선순위 낮은 +와 -은 나머지를 배출(단 괄호 제외)
    elif a[i]=='+' or a[i]=='-':
        if len(stack)!=0:
            while len(stack)!=0 and (stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-'):
                print(stack.pop(),end="")
        stack.append(a[i])
    
    elif a[i]=='(':
        stack.append(a[i])
    
    else:
        print(a[i],end="")

while len(stack)!=0:
    print(stack.pop(),end="")

