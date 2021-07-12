from itertools import combinations

heights = [int(input()) for _ in range(9)]
cases = combinations(heights, 7)

for case in cases:
    if sum(case) == 100:
        sorted_case = sorted(list(case))
        for height in sorted_case:
            print(height)

        break
