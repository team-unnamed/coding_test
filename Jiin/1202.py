"""
가방에는 보석을 하나만 넣을 수 있음
가방에는 무게 제한이 있음
보석은 각각 무게와 가치가 있음

가치 높은 순으로 정렬해서 그 보석의 무게와 가방 용랑 차이가 적은 쪽에 담는다
항상 모든 가방에 보석을 채울 수 있는 건 아니다

가치가 큰 보석을 작은 가방에 넣으면 이득이니까 작은 가방에 들어가는지를 먼저 확인

bisect.bisect(iterable, val) 대상 iterable의 정렬을 유지한 채로 val이 들어갈 수 있는 인덱스를 알려줌
다시 말해서 val보다 큰 최소값을 돌려준다는 것
주의! iterable은 정렬된 상태여야 함

iterable 안에 동일한 크기의 값이 여러 개 있을 경우에 bisect를 쓰면 (기본값 right) val이 들어갈 자리를 같은 값들 중 제일 오른쪽으로 잡는다
그럴 때는 bisect_left 쓰기

틀렸대... 왜? 반례찾아야함

아니면 heapq 알아보기
"""

import sys, bisect

N, K = map(int, sys.stdin.readline().split())

gems = []
for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gems.append((M,V))
gems = sorted(gems, key=lambda x: x[1], reverse=True)  # 가치순 정렬

bags = []
for i in range(K):
    bags.append(int(sys.stdin.readline()))

bags = sorted(bags)  # 작은 용량순으로 정렬

cnt = 0
stolen = 0

for gem in gems:
    LEN = len(bags)
    gem_m = gem[0]
    gem_v = gem[1]

    idx = bisect.bisect_left(bags, gem_m)  # 보석 무게보다 가방이 커야 하니까 idx번 가방에 넣기

    if idx != LEN:  # 구한 idx가 LEN이라는 건 그 어떤 가방에도 담을 수 없다는 뜻
        bags.pop(idx)
        cnt += 1
        stolen += gem_v

    if cnt == K:
        break

print(stolen)
