'''
무식하고 용감한 6중 반복문
'''

import sys

def fact(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res

def P(n,r):
    return fact(n) / fact(n-r)

def C(n,r):
    return P(n,r) / fact(r)

def calc(k, s):
    combination = []

    max_len = C(k, 6)
    cnt = 0
    for a in range(k):
        for b in range(a+1, k):
            for c in range(b+1, k):
                for d in range(c+1, k):
                    for e in range(d+1, k):
                        for f in range(e+1, k):
                            joined = ' '.join(map(str, [s[a], s[b], s[c], s[d], s[e], s[f]]))
                            combination.append(joined)
                            cnt += 1
                            if cnt == max_len:
                                return combination



while True:
    s = sys.stdin.readline()
    if s[0]=="0": break

    pool = list(map(int, s.split()))
    k = pool.pop(0)

    combination = calc(k, pool)
    for i in combination:
        print(i)

    print()
