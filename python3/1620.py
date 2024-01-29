import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

dictionary = {}
dictionary_rverse = {}
for i in range(n):
    temp=input().rstrip()
    dictionary[i+1]=temp
    dictionary_rverse[temp]=i+1
    
for i in range(m):
    temp = input().rstrip()
    try:
        print(dictionary[int(temp)])
    except:
        # print(dict(map(reversed,dictionary.items()))[temp])
        print(dictionary_rverse[temp])
        
#dictionary value로 람색할때
#dict(map(reversed, dictionary.items()))으로 탐색하면 됨
#단 dictionary.items()는 O(N)이 걸리는 함수니까 주의(dict는 O(1))