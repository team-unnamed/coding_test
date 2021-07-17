from itertools import combinations

l, c = map(int, input().split())
signs = sorted(input().split())

condition = ["a", "e", "i", "o", "u"]
ans = set()

for case in combinations(signs, l):
    vowel_size = sum(list(map(lambda x: x in condition, case)))
    if vowel_size >= 1 and len(case) - vowel_size >= 2:
        ans.add("".join(case))

for ans_ in sorted(ans):
    print(ans_)
