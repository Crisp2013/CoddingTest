##Python 3
# n = int(input())

# squares = set([])
# squares_2 = set([])
# sub_squares = set([])
# #제곱수
# t = 0
# while t**2 < n:
#     t = t + 1
#     squares.add(t**2)
#     sub_squares.add(n-t**2)

# #1번내 성공?
# if n in squares: 
#     print(1)
#     exit()

# #2번내 성공?
# for i in squares:
#     if i in sub_squares:
#         print(2)
#         exit()

# #3번내성공?
# for i in squares:
#     for j in squares:
#         if i+j in sub_squares:
#             print(3)
#             exit()


# print(4)


##PyPy
n = int(input())

lists = [5]*(n+2)

lists[0] = 0
lists[1] = 1

squares = set([])

t = 1
while t**2 <= n:
     squares.add(t**2)
     t = t + 1

worklists = set([i for i in range(2,50001)])

for i in range(2,n+1):
    worklists.remove(i)
    for k in (squares-worklists):
        lists[i] = min(lists[i], lists[i-k]+1)
    
print(lists[n])