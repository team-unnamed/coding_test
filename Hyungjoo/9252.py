"""
LCS(Longest Common Subsequence)
C_(i)(j)    = 0                             if i == 0 or j == 0
            = C_(i-1)(j-1) + 1              if i, j > 0 and x_i == y_i
            = max(C_(i-1)(j), C_(i)(j-1))   if i,j > 0 and x_i != y_i
"""

str_1 = input()
str_2 = input()
cache = [[0 for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]

for i in range(1, len(str_1) + 1):
    for j in range(1, len(str_2) + 1):
        if str_1[i - 1] == str_2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

ans = []
i, j = len(str_1), len(str_2)
while i > 0 and j > 0:
    if cache[i][j] == cache[i - 1][j]:
        i -= 1
    elif cache[i][j] == cache[i][j - 1]:
        j -= 1
    elif cache[i][j] == cache[i - 1][j - 1] + 1:
        ans.append(str_1[i - 1])
        i -= 1
        j -= 1

ans = "".join(reversed(ans))
print(len(ans))
if len(ans) > 0:
    print(ans)
