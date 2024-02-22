import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

true_know = list(map(int, input().split()))
true_know.pop(0)
#true_know = set(true_know)

party = dict()
person = dict()
party_check = [1]*(m+1)
party_check[0]=0

for i in range(1,n+1):
    person[i]=[]

for i in range(1,m+1):
    party[i] = list(map(int, input().split()))
    party[i].pop(0)
    for j in party[i]:
        person[j].append(i)

# print("party", party)
# print("person:", person)

work_list = true_know.copy()

while len(work_list)!=0:
    person_val = work_list.pop()

    party_arr = person[person_val]
    for i in party_arr:
        if party_check[i]==1:
            party_check[i]=0
            work_list = work_list + party[i]

print (sum(party_check))
