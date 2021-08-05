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
공백에 대한 대처
1. 시작점은 다음 step 일수록 3*2**s, 두번째 이어 붙이는 시작점은 N-3*2**s
2. 이러한 작업을 할시, 전 step에서 전달된 문자열들은 공백처리가 되어있지 않다. 이러한 점을 보완하고자, update 된 최대길이 만큼 padding

      
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