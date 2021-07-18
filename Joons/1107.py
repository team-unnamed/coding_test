"""
리모컨
시작 채널은 100 여기서 특정 버튼이 망가짐. 
망가진 상태로 키를 최소한 몇번 눌러야 해당 채널로 이동 할 수 있을지를 출력
채널은 0 에서 - 을 누를시 0 임, 채널의 수는 무한대

알고리즘
누르지 못하는 수를 고려햐여 최대한 해당 채널에 가까운 버튼 집합을 구하기.
가장 가까운수의 기준 min(해당채널 - 눌러서 진입한 채널)
제시된 수를 제외하고, 최대한의 숫자조합을 찾는것. 

dfs 로 구현될 경우 edge case : 만약 0을 사용하지 못한다면
1010
1
0 
인경우 999누르고 11번 누르는 것 5번 이정답인데
1111 을 최선이라고 뱉는다. 이를 고려하여 첫번째 자리수가 0이 될때도 들어 갈 수 있게 계산이 필요하다.
문자열을 밭아서 매번 받을때마다. 최솟값을 갱신하는 방법으로 접근.
"""
import sys

def dfs(c,step):
    global res
    for i in range(10):
        if buttons[i]:
            cur_channel = c + str(i)
            res = min(res, abs(int(cur_channel)-channel)+len(cur_channel))
            if step < max_length:    
                dfs(cur_channel,step+1)        

input = sys.stdin.readline
channel = int(input())
n = int(input())
if n == 10:
    print(abs(100-channel))
else:
    buttons = [1]*10
    malfunction = list(map(int,input().split()))
    for i in malfunction:
        buttons[i] = 0

    max_length = len(str(channel))
    res = abs(100-channel)            
    set_button = ['0']*max_length
    dfs('',0)
    print(res)



