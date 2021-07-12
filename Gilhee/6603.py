from itertools import combinations

while True:
    x = input()
    if x=='0':
        break

    x = list(map(int,x.split()))
    k = x[0]
    S = x[1:]

    comb = list(combinations(S, 6))

    for i in comb:
        for j in i:
            print(j, end=' ')
        print()
    print()