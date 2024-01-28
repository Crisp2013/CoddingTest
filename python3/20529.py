import sys
input = sys.stdin.readline


def diff(str1, str2):
    value = 0 
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            value = value + 1
    return value

t = int(input())
for i in range(t):
    n = int(input())
    lists = input().split()

    answer = 9999
    if n >= 48:
        answer = 0
    # elif n > 16:
    #     for i in range(len(lists)):
    #         for j in range(i+1,len(lists)):
    #             answer = min(answer, diff(lists[i],lists[j]))

    else:
        for i in range(len(lists)):
            for j in range(i+1,len(lists)):
                for k in range(j+1,len(lists)):
                    answer = min(answer, diff(lists[i],lists[j])+diff(lists[j],lists[k])+diff(lists[i],lists[k]))
    print(answer)