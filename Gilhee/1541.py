import sys
input = sys.stdin.readline

equation_m = input().rstrip('\n').split('-')

answer = sum(map(int,equation_m.pop(0).split('+')))
for i, equation in enumerate(equation_m):
    answer -= sum(map(int,equation.split('+')))

print(answer)