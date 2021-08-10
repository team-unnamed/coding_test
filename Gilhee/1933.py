import sys
import heapq
input = sys.stdin.readline

n = int(input())
mem = []
x=set()

for i in range(n):
    l, h, r = map(int, input().rstrip('\n').split())
    mem.append([l,h,r])
    x.add(l)
    x.add(r)
    
mem.sort()
x = sorted(list(x))

height = 0
heap = []
for i in x:
    
    while mem:
        if mem[0][0]>i:
            break
        l, h, r = mem.pop(0)
        heapq.heappush(heap, [-h, r])

    while heap:
        if heap[0][1]<=i:
            heapq.heappop(heap)
        else:
            break
    
    current_height=0

    if heap != []:
        current_height = -heap[0][0]
    
    if height != current_height:
        print(i, current_height, end=' ')

    height = current_height
