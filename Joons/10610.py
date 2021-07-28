# 30 
import sys
input = sys.stdin.readline

n = [int(s) for s in input().split()[0]]
if (sum(n) % 3 != 0) or not(0 in n):
    print(-1)
else:
    print(''.join(sorted(map(str,n), reverse=True)))