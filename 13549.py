"""
걸으면 1초 후에 x+1이나 x-1 위치
순간이동을 하면 0초 후에 2x 위치

N==K / N>K / N<K

한 턴에2x, x-1, x+1 순서로 이동하면서 0-1 bfs (코스트가 0인 걸 먼저 해 본다)
어차피 순간이동하면 턴을 더 적게 쓸 테니까 그냥 K 위치 가자마자 리턴

"""

import sys, collections

def bfs(N, K):
    q = collections.deque()
    q.append(N)

    time_arrive = [-1 for _ in range(LIMIT)]
    time_arrive[N] = 0

    while q:
        current_pos = q[0]
        q.popleft()
        time_ = time_arrive[current_pos]
        
        if current_pos == K:
            return time_

        # 순간이동
        next_pos = current_pos * 2
        if next_pos < LIMIT and time_arrive[next_pos] == -1:
            q.appendleft(next_pos)  # 순간이동은 코스트가 0이라서 우선적으로 고려
            time_arrive[next_pos] = time_

        # x-1
        next_pos = current_pos - 1
        if 0 <= next_pos < LIMIT and time_arrive[next_pos] == -1:
            q.append(next_pos)
            time_arrive[next_pos] = time_ + 1

        # x+1
        next_pos = current_pos + 1
        if next_pos < LIMIT and time_arrive[next_pos] == -1:
            q.append(next_pos)
            time_arrive[next_pos] = time_ + 1



N, K = map(int, sys.stdin.readline().split())
LIMIT = 200_001

if N==K:
    res = 0
elif N>K:
    res = N-K
else:
    res = bfs(N,K)

print(res)

