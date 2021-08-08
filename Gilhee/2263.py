import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
Inorder = list(map(int, input().rstrip('\n').split()))
Postorder = list(map(int, input().rstrip('\n').split()))
index = [0 for _ in range(n+1)]

for i in range(n):  
    index[Inorder[i]] = i


def tree(instart, inend, poststart, postend):
    if instart==inend:
        print(Inorder[instart], end=' ')
        return 
    elif instart>inend:
        return
    root = Postorder[postend]
    print(root, end=' ')

    divide = index[root]
    gap = instart-poststart

    tree(instart, divide-1, poststart, divide-1-gap)
    tree(divide+1, inend, divide-gap, postend-1)

tree(0, len(Inorder)-1, 0, len(Postorder)-1)
