import sys
from itertools import permutations

input = sys.stdin.readline

# 조건1: 최소 한 개의 모음, 최소 두 개의 자음으로 구성 되어야 함.
def vowelcheck(passward):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    cons_count = 0
    for p in passward:
        if p in vowels:
            vowel_count += 1
        else:
            cons_count += 1

    if (vowel_count >= 1) and (cons_count >= 2):
        return True
    else:
        return False

# 조건2: 알파벳이 증가하는 순서로 배열되어 있어야 함
def ordercheck(passward):
    prev = "a"
    for p in passward:
        if p < prev:
            return False
        prev = p

    return True


L, C = map(int, input().rstrip("\n").split(" "))
alphabet = list(map(str, input().rstrip("\n").split(" ")))

comb = sorted(list(permutations(alphabet, L))) # 모든 암호 조합을 list로 저장 후 알파벳 순으로 정렬
for passward in comb:
    if vowelcheck(passward) and ordercheck(passward):
        print("".join(passward))
