import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
root = int(input())
tree = dict()
tree[root]=[-1,-1]
while True:
    try:
        temp = int(input())

        cur_root = root
        while True:
            if temp < cur_root:
                if tree[cur_root][0] == -1:
                    tree[cur_root][0] = temp
                    tree[temp] = [-1,-1]
                    break
                else:
                    cur_root = tree[cur_root][0]
                    

            else:#temp > cur_root:
                if tree[cur_root][1] == -1:
                    tree[cur_root][1] = temp
                    tree[temp] = [-1,-1]
                    break
                else:
                    cur_root = tree[cur_root][1]
    except:
        break

def dfs(cur_root):
    if tree[cur_root][0]!=-1:
        dfs(tree[cur_root][0])
    if tree[cur_root][1]!=-1:
        dfs(tree[cur_root][1])
    print(cur_root)

dfs(root)

