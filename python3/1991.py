n = int(input())

tree = dict()

for i in range(n):
    temp = input().split()
    tree[temp[0]] = (temp[1],temp[2])
    
    
first = []
last = []
mid = []

def tree_fuc(temp):
    
    first.append(temp)
    if tree[temp][0]!=".":
        tree_fuc(tree[temp][0])
    mid.append(temp)
    if tree[temp][1]!=".":
        tree_fuc(tree[temp][1])
    last.append(temp)
        
tree_fuc("A")
        
print("".join(first))
print("".join(mid))
print("".join(last))