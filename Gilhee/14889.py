from copy import deepcopy

def dif(temp1):
    global result
    temp2 = []
    for i in range(n):
        if i in temp1:
            continue
        temp2.append(i)
    temp1_n = 0
    temp2_n = 0
    for i in range((n // 2) - 1):
        for j in range(i + 1, n // 2):
            a, b = temp1[i], temp1[j]
            c, d = temp2[i], temp2[j]
            temp1_n += s[a][b] + s[b][a]
            temp2_n += s[c][d] + s[d][c]
    result = min(result, abs(temp1_n - temp2_n))
def dfs(temp):
    t = deepcopy(temp)
    if len(t) == n // 2:
        dif(t)
        return
    for i in range(t[-1] + 1, n):
        t.append(i)
        dfs(t)
        t.pop()
n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
result = 1000000000
temp = [0]
dfs(temp)
print(result)