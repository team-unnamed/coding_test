[L, C] = list(map(int, input().split()))

characters = input().split()

case = []
all_cases = []
characters.sort()

def solve(depth, idx, L, C):
    if depth == L:
        all_cases.append(''.join(map(str, case)))
        return
    for i in range(idx, C):
        case.append(characters[i])
        solve(depth+1, i+1, L, C)
        case.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

solve(0, 0, L, C)
password(all_cases)