"""
55-50+40 > 55-(50+40)
적절하게 괄호를 쳐서 식의 값을 최소로 만들기

20+40-(30+50+70)-5420
- 다음에 오는 값이 크면 좋다

20+40 - (30+50+70-5+4200)
이런 경우에는 어쩌지?

헐 괄호 여러개 써도 됨 그럼 무조건 - 뒤에 있는 놈들 다 괄호쳐

숫자가 0으로 시작할 수도 있음...
"""

import sys

s = sys.stdin.readline()

s_list = s.split('-')
LEN = len(s_list)

max_sum = 0
idx = 0
for i, chunk in enumerate(s_list):
    s_list[i] = str(sum(map(int, chunk.split('+'))))

s = '-'.join(s_list)
print(eval(s))
