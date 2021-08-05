"""
별찍기
N 은 3x2**k 의 형태이다. 

특징!
- N은 첫째줄 * 의 출력 위치 이다.
k == 4
3*16
16 3개 ( 8 3개 2개 )
8 3개 ( 4 3개 2개 )
4 3개 ( 1 3개 2개 )
2 3개 

들여 쓰기 맟추기도 필요.

"""

"""
1. 최 상단의 트리를 그린다. (시작 위치 중요)
2. 이를 다음 단계에서 기존의 트리를 가지고 더 붙이는 작업을 한다. 
하지만 이는 어찌 해야 좋을지 가 의문이다

      
     *      
    * *     
   *****    
  *     * (3, 2)
 * *   * * (2, 1)
***** ***** (1, 0)
"""
import sys
input = sys.stdin.readline

N = int(input())

# 별 트리 하나 그리기
def draw_star(start):
    s = []
    s.append(' '*(start-1)+'*'+'  ')
    s.append(' '*(start-2)+'* *'+' ')
    s.append(' '*(start-3)+'*'*5)
    return s
def draw_star_pair(stars,f,s):
    tmp_l = len(stars)
    for i in range(len(stars)):
        stars.append(stars[i][f:] + ' ' + stars[i][s:])
    for t in range(tmp_l):
        stars[t] = stars[t]+' '*(len(stars[-1])-len(stars[t]))
    return stars

def solution(N):
    if N == 3:
        return draw_star(3)
    else:
        res = draw_star(N)
        f = 3
        s = N-3
        while s: 
            res = draw_star_pair(res, f,s)
            f *= 2
            s = N-f
    return res
tmp = solution(N)
for i in tmp:
    print(i)
# draw_star_pair(draw_star(12),12)

# 6 --> 6-3 // 
# 12 --> 12-3 --> 12-3-3