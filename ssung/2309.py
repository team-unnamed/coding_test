"""

일곱 난쟁이의 키의 합이 100이므로 모든 경우의 수를 구하면 됨.
총 9명의 난쟁이가 있으므로 전체 합에서 2명의 키를 뺀 값이 100이 되면 된다.

"""
import sys

input = sys.stdin.readline


def bruteforce(dwarf):
    height = sum(dwarf)
    for i in range(9):
        for j in range(i):
            if height - (dwarf[i] + dwarf[j]) == 100: # 두 난쟁이를 뺀 값이 100이면 일곱 난쟁이를 찾을 수 있음
                del dwarf[i]
                del dwarf[j]
                dwarf.sort() # 오름차순정렬

                return dwarf


dwarf = []
for _ in range(9):
    dwarf.append(int(input().rstrip("\n")))

result = bruteforce(dwarf)

for h in result:
    print(h)
