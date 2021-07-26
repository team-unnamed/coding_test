"""
양수 N의 자리 숫자를 섞어서 30의 배수 만들기
우선 2의 배수인지, 3의 배수인지, 5의 배수인지 확인 > 이것들의 배수가 아니면 제낀다
이걸 모두 만족하려면 숫자들 다 더해서 3의 배수여야 하고, 10의 배수여야 하니까 0이 포함되어 있어야 함
각 자리수의 합이 3의 배수라면 무조건 3의 배수인가? > 그런듯?

끝자리에 0 고정하고 나머지 숫자 정렬해서 큰 순서대로 때려박으면 끝
"""


import sys

N = sys.stdin.readline().strip()
digit = list(map(int, list(N)))
digit.sort(reverse=True)

if digit[-1] != 0:
    print(-1)

elif sum(digit)%3 != 0:
    print(-1)

else:
    for i in digit:
        print(i, end="")

