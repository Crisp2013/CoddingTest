n = int(input())

height = list(map(int, input().split()))

#오른쪽 왼쪽의 tan 값을 비교하면 되는 문제가 아닌지?
build = [0]*len(height)

for i in range(len(height)):
    left_tan = -10e9
    right_tan = -10e9
    for j in reversed(range(0,i)):
        if (height[j]-height[i])/abs(i-j)>left_tan:
            build[i]+=1
            left_tan = (height[j]-height[i])/abs(j-i)

    for j in range(i+1,len(height)):
        if (height[j]-height[i])/abs(j-i)>right_tan:
            build[i]+=1
            right_tan = (height[j]-height[i])/abs(j-i)

print(max(build))
    