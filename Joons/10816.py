# 숫자 카드 2
import sys
from collections import Counter
input = sys.stdin.readline


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
cs = list(map(int, input().split()))


res = dict(Counter(cards))

print(' '.join([str(res.get(c,0)) for c in cs]))


