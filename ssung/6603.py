"""

itertools의 combinations를 사용하면 간단하게 풀 수 있다. (라이브러리 없이도 풀어보자)

"""
import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    lottery = list(map(int, input().rstrip("\n").split(" ")))
    if lottery[0] == 0:
        break

    del lottery[0]
    result = list(combinations(lottery, 6)) # combinations 사용
    for temp in result:
        print(" ".join(map(str, temp))) # tuple은 join이 안되니 str type으로 변경
    print()
