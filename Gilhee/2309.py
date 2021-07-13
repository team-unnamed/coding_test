from itertools import combinations

length = []

for _ in range(9):
    length.append(int(input()))

for comb in combinations(length, 7):
    if sum(comb)==100:
        for c in sorted(list(comb)):
            print(c)
        break