import sys
input = sys.stdin.readline
def quick_sort(start,end):
    if end-start<1:
        return
    if end-start==2:
        if lists[start]>lists[end]:
            (lists[start],lists[end])=(lists[end],lists[start])
            return
    low=start+1
    high=end
    
    pivot = lists[start]
    while high>low:
        while low<end and lists[low]<pivot:
            low=low+1
        while high>start and lists[high]>pivot:
            high=high-1
        
        if low<high:
            (lists[high],lists[low])=(lists[low],lists[high])
        
    
    # print(start,end,low,high,lists)
    (lists[high],lists[start])=(lists[start],lists[high])
    quick_sort(start,high-1)
    quick_sort(high+1,end)

n = int(input().split()[0])

lists = []
for i in range(n):
    lists.append(int(input().split()[0]))
lists = sorted(lists)
# quick_sort(0,len(lists)-1)

for i in range(n):
    print(lists[i])
