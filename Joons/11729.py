"""
하노이 탑 쌓기.
1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓ㄹ은 원판은 항상 위의 것이 아래의 것보다 작아야 한다. 

input : 첫번째 장대에 놓인 탑의 갯수
output : 총 시행 횟수(최솟값) 및 시행 결과

n = 1
1 3 // 

n = 2 
1 2 
1 3 //
2 3

n = 3
1 3 
1 2
3 2
1 3 //
2 1
2 3
1 3

n = 4
1 3
1 2
2 3




# 규칙 1
가장 긴 막대가 3번에 위치 하게끔 되어야 한다. 

# 규칙 2
3번 장대에 가장 긴 블럭이 들어가려면, 나머지 장대 아무것도 없었던 장대에 가장 긴 블럭을 제외하고
순서대로 쌓여져 있어야 한다. 

규칙 1 과 2를 반복적으로 수행한다.
근데 이게왜 분할정복이냐 : 항상 최선의 선택 --> 최 하단의 블럭이 해당 블럭에 있게끔..


n = 1
바로 이동
n = 2
옮겨주고 이동

n = 3
옮기려는 곳에 바로 옮기기
1 3

n = 4
4 1->3
    3 1->2 4
        2 1->3 2,3
        1 1->2 1
        2 3->2 6,7
        1 3->1 5



"""
# 블럭을 해당 장대에 옮기는 함수.
# 재귀 함수를 사용하는 것이 좋을듯

import sys
input = sys.stdin.readline
N = int(input())
# top = [[0],[0],[0]]
# for i in range(N,0,-1):
#     top[0].append(i)

cnt = 0
log = []
def move_bottom(start,target,block):
    global cnt, log
    ## start : 0 taget : 2 block : 3

    # 이전의 것들 다 옮기고,
    if block != 1: 
        for b in range(3):
            if b not in (start, target):
                move_bottom(start,b,block-1)

    # 해당 블럭만 원하는 위치에 옮기고
    log.append(f"{start+1} {target+1}")
    cnt += 1

    # 원래대로 복구하기.
    if block != 1 :
        for b in range(3):
            if b not in (start, target):
                move_bottom(b, target, block-1)
    

move_bottom(0,2,N)
print(cnt)
for i in log:
    print(i)
