'''
itertools의 combination으로 암호 후보군을 싹 구한다
구하기 전에 받은 문자열을 정렬해놓으면 조합 구할 때 알아서 사전순으로 해 줌
자음/모음 규칙에 어긋나는 놈들을 빼고 출력
WA!
'''


import sys, itertools

L, C = map(int, sys.stdin.readline().split())
vowel = {'a','e','i','o','u'}
s = sys.stdin.readline().split()
s.sort()

candidate = itertools.combinations(s, L)
for i in candidate:
    code = set(i)
    if (vowel & code) and (len(code - vowel) >= 2):  # 모음 1개, 자음 2개 이상 필요
        password = "".join(i)
        print(password)
