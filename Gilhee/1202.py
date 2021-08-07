import heapq

N, K = map(int, input().split())
gem = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gem, [weight, value])

bag = []    
for _ in range(K):
    capacity = int(input())
    heapq.heappush(bag, capacity)

total_value = 0 
capable_gem = [] 

for _ in range(K):
    capacity = heapq.heappop(bag)
    
    while gem and capacity >= gem[0][0]: 
        [weight, value] = heapq.heappop(gem) 
        heapq.heappush(capable_gem, -value)
    
    if capable_gem: 
        total_value -= heapq.heappop(capable_gem)
    elif not gem:
        break

print(total_value)